from gensim.models.doc2vec import LabeledSentence
from gensim import models
from gensim.models import Doc2Vec
import jieba
import jieba.analyse


def split_function():
    """
    分割文本并且去除\
    """
    with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/199801utf8.txt") as read_file:
        with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/199801utf8split.txt", "w") as write_file:
            for line in read_file:
                # 通过空格分割文本
                string = line.split()
                result = str()
                # 去除分词后面的词属性
                for index, s in enumerate(string):
                    if index is 0:
                        result += s[:s.index('/')] + ' '
                        continue
                    result += s[:s.index('/')]
                write_file.write(result + '\n')


def del_time_function():
    """
    得到去除前面日期的文本
    """
    with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/199801utf8split.txt") as read_file:
        with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/199801utf8split_del_time.txt", "w") as write_file:
            for line in read_file:
                if len(line) <= 1:
                    continue
                # 通过空格分割文本
                string = line.split()
                string = string[1]
                write_file.write(string + '\n')


def remove_english_function():
    """
    去除维基百科数据中开头是英文的数据
    :return:
    """
    with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/data/wiki.zh.text_with_blank.utf-8") as read_file:
        with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/data/wiki.zh.text_with_blank.del_english.utf-8",
                  "w") as write_file:
            import re
            import jieba
            jieba.load_userdict('./dict.txt')
            jieba.analyse.set_stop_words('./stopwords.dic')
            pattern = '(^Wiki)|(^Help)|(__NOED)|(^// )|(^http:)'
            for line in read_file:
                if len(line) <= 1:
                    continue
                if len(re.findall(pattern, line)) is 0:
                    words = jieba.analyse.extract_tags(line, topK=1000)
                    if len(words) < 3:
                        continue
                    write_file.write(line)


def get_train_data_function():
    """
    通过文本生成符合LSTM训练的材料
    """
    with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/199801utf8split.txt") as read_file:
        with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/199801_utf8_train.txt", "w") as write_file:
            import re
            p = re.compile(r'，|。|？|！')
            for line in read_file:
                if len(line) <= 1:
                    continue
                # 去除文章前面的日期
                string = line.split()
                string = string[1]
                # 通过，和。分割文本
                result_list = p.split(string)
                length = len(result_list)
                # 特殊处理一些最后一个字符可能有。可能没有。
                if len(result_list[length - 1]) < 2:
                    result_list = result_list[:-1]
                    length = len(result_list)
                for index, s in enumerate(result_list):
                    # 如果索引等于列表长度，输出为分割线即1
                    if index + 1 is length:
                        write_file.write(s + ' 1' + '\n')
                    # 否则输出0
                    else:
                        write_file.write(s + ' 0' + '\n')


def train_line_data_function():
    """
    通过文本生成符合LSTM训练的材料
    """
    with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/199801utf8split.txt") as read_file:
        with open("/home/jxxiangwen/util/windows 7/迅雷下载/199801/199801_utf8_train_line.txt", "w") as write_file:
            import re
            p = re.compile(r'。|？|！')
            for line in read_file:
                if len(line) <= 1:
                    continue
                # 去除文章前面的日期
                string = line.split()
                string = string[1]
                # 通过，和。分割文本
                result_list = p.split(string)
                length = len(result_list)
                # 特殊处理一些最后一个字符可能有。可能没有。
                if len(result_list[length - 1]) < 2:
                    result_list = result_list[:-1]
                    length = len(result_list)
                for index, s in enumerate(result_list):
                    jieba.load_userdict('./dict.txt')
                    jieba.analyse.set_stop_words('./stopwords.dic')
                    words = jieba.analyse.extract_tags(s, topK=1000)
                    if len(words) < 3:
                        continue
                    # 如果索引等于列表长度，输出为分割线即1
                    if index + 1 is length:
                        write_file.write(s + '\n')
                    # 否则输出0
                    else:
                        write_file.write(s + '\n')


class MySentences(object):
    def __init__(self, dir_name):
        self.dir_name = dir_name

    def __iter__(self):
        import os
        for file_name in os.listdir(self.dir_name):
            for line in open(os.path.join(self.dir_name, file_name)):
                yield line.split()[1]


class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        for uid, line in enumerate(open(self.filename)):
            jieba.load_userdict('./dict.txt')
            jieba.analyse.set_stop_words('./stopwords.dic')
            words = jieba.analyse.extract_tags(line, topK=1000)
            yield LabeledSentence(words=words, labels=['SENT_%s' % uid])


def train_doc2vec():
    """
    训练doc2vec模型
    :return:
    """
    model = models.Doc2Vec(alpha=.025, min_alpha=.025, min_count=1)
    renmin_path = "/home/jxxiangwen/util/windows 7/迅雷下载/199801/data/199801_utf8_train_line.txt"
    sentences = LabeledLineSentence(renmin_path)
    model.build_vocab(sentences)

    for epoch in range(10):
        model.train(sentences)
        model.alpha -= 0.002  # decrease the learning rate`
        model.min_alpha = model.alpha  # fix the learning rate, no decay

    model.save("my_model.doc2vec")
    wiki_path = "/home/jxxiangwen/util/windows 7/迅雷下载/199801/data/wiki.zh.text_with_blank.del_english.utf-8"


if __name__ == "__main__":
    # split_function()
    # train_data_function()
    # del_time_function()
    # remove_english_function()
    # train_line_data_function()
    train_doc2vec()