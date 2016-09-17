import numpy as np
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, ShuffleSplit
from sklearn.ensemble import RandomForestRegressor
import time


class Gene(object):
    def __init__(self):
        self.encode_dict = dict()
        self.label = list()
        self.data_set = list()
        self.class_name = list()
        self.multi_phenos = list()
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None

    def get_data_set(self):
        """
        设置数据集
        :return: None
        """
        i = 0
        with open('genotype.dat') as genotype:
            for line in genotype:
                if 0 == i:
                    self.label = line.strip().split(' ')
                    i += 1
                else:
                    self.data_set.append(line.strip().split(' '))
        self.label = np.array(self.label)
        self.data_set = np.array(self.data_set)

    def get_class_set(self):
        """
        设置类集
        :return:None
        """
        with open('phenotype.txt') as phenotype:
            for line in phenotype:
                self.class_name.append(int(line.strip().split(' ')[0]))
        self.class_name = np.array(self.class_name)

    def get_multi_set(self):
        """
        设置类集
        :return:None
        """
        with open('multi_phenos.txt') as multi_phenos:
            for line in multi_phenos:
                self.multi_phenos.append(line.strip().split(' '))

        row = len(self.multi_phenos)
        column = len(self.multi_phenos[0])
        for i in range(row):
            for j in range(column):
                self.multi_phenos[i][j] = int(self.multi_phenos[i][j])
        self.multi_phenos = np.array(self.multi_phenos)

    def encode_three(self, string):
        """
        数据编码信息：相同为0或者2，不同为1
        :param string: 原始字符串
        :return: 编码后数字
        """
        if 2 != len(string):
            raise ValueError('字符串长度必须为2')
        code = self.encode_dict.get(string)
        if code is None:
            if string[0] == string[1]:
                values = list(self.encode_dict.values())
                if values.count(0) is 0:
                    self.encode_dict[string] = 0
                if values.count(2) is 0:
                    self.encode_dict[string] = 2
            else:
                self.encode_dict[string] = 1
        return self.encode_dict.get(string)

    def get_encode_data(self):
        """
        把数据编码
        :return: None
        """
        row = len(self.data_set)
        column = len(self.data_set[0])
        for i in range(column):
            for j in range(row):
                self.data_set[j][i] = self.encode_three(self.data_set[j][i])
            self.encode_dict = dict()

    def produce_encode_file(self):
        """
        生编码后的文件
        :return:
        """
        file_name = 'three_encode.dat'
        length = len(self.label)
        with open(file_name, 'w') as three_encode:
            for (index, name) in enumerate(self.label):
                if index != length - 1:
                    three_encode.write(name + '\t')
                else:
                    three_encode.write(name)
            three_encode.write('\n')
            for row in self.data_set:
                for (index, value) in enumerate(row):
                    if index != length - 1:
                        three_encode.write(str(value) + '\t')
                    else:
                        three_encode.write(str(value))
                three_encode.write('\n')

    def get_entropy_tree(self, file_name='with_A', class_result=None):
        """
        使用entropy生成决策树
        :param class_result: 使用的分类结果
        :param file_name: 结果写入的文件
        :return: None
        """
        # 拆分训练数据与测试数据
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.data_set, self.class_name,
                                                                                test_size=0.2)
        # 使用信息熵作为划分标准，对决策树进行训练
        clf = tree.DecisionTreeClassifier(criterion='entropy')
        print(clf)
        clf.fit(self.x_train, self.y_train)

        # # 获得当前时间时间戳
        # now = int(time.time())
        # # 把决策树结构写入文件
        # file_name = 'entropy_tree' + str(now) + '.dot'
        # with open(file_name, 'w') as tree_file:
        #     tree.export_graphviz(clf, out_file=tree_file)

        # 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大
        times = 0
        result_list = list()
        file_name = 'entropy_decision_tree_' + file_name + '.dot'
        with open(file_name, 'w') as import_file:
            for (index, i) in enumerate((list(clf.feature_importances_))):
                if i > 0:
                    result_list.append(tuple((self.label[index], float(i))))
                    # times += 1
                    # import_file.write(self.label[index] + '   ')
            result_list.sort(key=lambda x: x[1], reverse=True)
            for (index, result) in enumerate(result_list):
                import_file.write(str(index) + '\t' + str(result[0]) + '\t' + str(result[1]) + '\n')
            import_file.write('\n')
        print(clf.feature_importances_)
        print('特征数目：', times)

        # 测试结果的打印
        answer = clf.predict(self.x_train)
        # print(len(self.x_train))
        # print(answer)
        # print(len(self.y_train))
        # print(np.mean(answer == self.y_train))

        # 准确率与召回率
        precision, recall, thresholds = precision_recall_curve(self.y_train, clf.predict(self.x_train))
        print('准确率：', precision)
        print('召回率：', recall)
        print('阈值：', thresholds)
        answer = clf.predict_proba(self.data_set)[:, 1]
        print(classification_report(self.class_name, answer, target_names=['Not Sick', 'Sick']))

    def get_gini_tree(self, file_name='with_A', class_result=None):
        """
        使用gini生成决策树
        :param file_name: 结果写入的文件
        :param class_result: 使用的分类结果
        :return:None
        """
        # 拆分训练数据与测试数据
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.data_set, self.class_name,
                                                                                test_size=0.2)
        # 使用信息熵作为划分标准，对决策树进行训练
        clf = tree.DecisionTreeClassifier()
        print(clf)
        clf.fit(self.x_train, self.y_train)

        # # 获得当前时间时间戳
        # now = int(time.time())
        # # 把决策树结构写入文件
        # file_name = 'gini_tree' + str(now) + '.dot'
        # with open(file_name, 'w') as tree_file:
        #     tree.export_graphviz(clf, out_file=tree_file)

        # 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大
        times = 0
        result_list = list()
        file_name = 'gini_decision_tree_' + file_name + '.dot'
        with open(file_name, 'w') as import_file:
            for (index, i) in enumerate((list(clf.feature_importances_))):
                if i > 0:
                    result_list.append(tuple((self.label[index], float(i))))
                    # times += 1
                    # import_file.write(self.label[index] + '   ')
            result_list.sort(key=lambda x: x[1], reverse=True)
            for (index, result) in enumerate(result_list):
                import_file.write(str(index) + '\t' + str(result[0]) + '\t' + str(result[1]) + '\n')
            import_file.write('\n')
        print(clf.feature_importances_)
        print('特征数目：', times)

        # 测试结果的打印
        answer = clf.predict(self.x_train)
        # print(len(self.x_train))
        # print(answer)
        # print(len(self.y_train))
        # print(np.mean(answer == self.y_train))

        # 准确率与召回率
        precision, recall, thresholds = precision_recall_curve(self.y_train, clf.predict(self.x_train))
        print('准确率：', precision)
        print('召回率：', recall)
        print('阈值：', thresholds)
        answer = clf.predict_proba(self.data_set)[:, 1]
        print(classification_report(self.class_name, answer, target_names=['Not Sick', 'Sick']))

    def get_by_random_forest(self, file_name='with_A', class_result=None):
        """
        随机森林特征选择
        :param file_name: 结果写入的文件
        :param class_result: 使用的分类结果
        :return:
        """
        rf = RandomForestRegressor()
        scores = []
        for i in range(self.data_set.shape[1]):
            score = cross_val_score(rf, self.data_set[:, i:i + 1], self.class_name, scoring="r2",
                                    cv=ShuffleSplit(len(self.data_set), 3, .3))
            scores.append((round(np.mean(score), 3), self.label[i]))
        scores = sorted(scores, reverse=True)

        # 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大
        file_name = 'random_forest_' + file_name + '.dot'
        with open(file_name, 'w') as import_file:
            times = 0
            for (index, result) in enumerate(scores):
                if times < 80:
                    import_file.write(str(index) + '\t' + str(result[1]) + '\t' + str(result[0]) + '\n')
                    times += 1
                else:
                    break
            import_file.write('\n')

    def get_by_recursive_feature_elimination(self, file_name='with_A', class_result=None):
        """
        递归特征消除特征选择
        :param file_name: 结果写入的文件
        :param class_result: 使用的分类结果
        :return:None
        """
        from sklearn.feature_selection import RFE
        from sklearn.linear_model import LinearRegression
        lr = LinearRegression()
        # rank all features, i.e continue the elimination until the last one
        rfe = RFE(lr, n_features_to_select=1)
        rfe.fit(self.data_set, self.class_name)

        scores = sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), self.label))

        # 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大
        file_name = 'recursive_feature_elimination_' + file_name + '.dot'
        with open(file_name, 'w') as import_file:
            times = 0
            for (index, result) in enumerate(scores):
                if times < 80:
                    import_file.write(str(index) + '\t' + str(result[1]) + '\t' + str(result[0]) + '\n')
                    times += 1
                else:
                    break
            import_file.write('\n')

    def get_by_stability_selection(self, file_name='with_A', class_result=None):
        """
        稳定性选择特征选择
        :param file_name: 结果写入的文件
        :param class_result: 使用的分类结果
        :return:None
        """
        from sklearn.linear_model import RandomizedLasso

        lasso = RandomizedLasso()
        lasso.fit(self.data_set, self.class_name)

        scores = sorted(zip(map(lambda x: round(x, 4), lasso.scores_),
                            self.label), reverse=True)
        # 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大
        file_name = 'stability_selection_' + file_name + '.dot'
        with open(file_name, 'w') as import_file:
            times = 0
            for (index, result) in enumerate(scores):
                import_file.write(str(index) + '\t' + str(result[1]) + '\t' + str(result[0]) + '\n')
                # if times < 80:
                #     import_file.write(str(index) + '\t' + str(result[1]) + '\t' + str(result[0]) + '\n')
                #     times += 1
                # else:
                #     break
            import_file.write('\n')

    @staticmethod
    def get_union_from_result(result_dir='result', union_file='with_A'):
        """
        将五种算法的结果取并集
        :param result_dir: 结果所在文件夹
        :param union_file: 5种算法交集存储文件夹
        :return:
        """
        # 最终交集后的set
        final_set = set()
        import os
        file_name = result_dir
        for index, files in enumerate(os.listdir(file_name)):
            with open(result_dir + os.path.sep + files) as result_file:
                temp_set = set()
                for line in result_file:
                    # 跳过空行
                    if line is None or len(line) < 2:
                        continue
                    temp_set.add(line.strip().split('\t')[1])
            if index is 0:
                # 初始化
                final_set = temp_set
            else:
                # 交集
                final_set = final_set.intersection(temp_set)

        file_name = 'union_' + union_file + '.dot'
        with open(file_name, 'w') as union_file:
            for order_number, value in enumerate(final_set):
                union_file.write(str(order_number) + '\t' + str(value) + '\n')

    @staticmethod
    def get_gene():
        """
        得到相关的基因
        :return:
        """
        # 最终的set
        final_set = set()
        import os
        file_name = 'gene_info'
        union_name = 'union_with_A.dot'
        with open(union_name) as union_file:
            # 遍历交集
            for union in union_file:
                gene = union.strip().split('\t')[1]
                if len(gene) > 3:
                    for files in os.listdir(file_name):
                        with open(file_name + os.path.sep + files) as result_file:
                            for line in result_file:
                                # 跳过空行
                                if line is None or len(line) < 2:
                                    continue
                                if line.count(gene) > 0:
                                    final_set.add(files)
                                    break
        file_name = 'gene_with_A.dot'
        with open(file_name, 'w') as union_file:
            for order_number, value in enumerate(final_set):
                union_file.write(str(order_number) + '\t' + str(value) + '\n')


if __name__ == '__main__':
    g = Gene()
    # 数据与处理
    # g.get_data_set()
    # g.get_class_set()
    # g.get_encode_data()
    # g.get_multi_set()
    # 5种算法
    # g.get_entropy_tree()
    # g.get_gini_tree()
    # g.get_by_random_forest()
    # g.get_by_recursive_feature_elimination()
    # g.get_by_stability_selection()
    # 得到算法交集
    # Gene.get_union_from_result()
    # 得到第3题结果
    # Gene.get_gene()
    # 第4题处理
    # for index in range(len(g.multi_phenos[0])):
    #     g.get_entropy_tree(file_name='with_' + str(index), class_result=g.multi_phenos[:, index])
    #     g.get_gini_tree(file_name='with_' + str(index), class_result=g.multi_phenos[:, index])
    #     g.get_by_random_forest(file_name='with_' + str(index), class_result=g.multi_phenos[:, index])
    #     #g.get_by_recursive_feature_elimination(file_name='with_' + str(index), class_result=g.multi_phenos[:, index])
    #     g.get_by_stability_selection(file_name='with_' + str(index), class_result=g.multi_phenos[:, index])
    # 第4题结果取交集
    for index in range(10):
        Gene.get_union_from_result(result_dir=str(index), union_file='with_' + str(index))
