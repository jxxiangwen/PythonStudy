if __name__ == '__main__':
    import jieba
    import jieba.analyse
    jieba.load_userdict('./dict.txt')
    jieba.analyse.set_stop_words('./stopwords.dic')
    # seg_list_iterator = jieba.cut('就其本身而言，你和他')  # 默认是精确模式
    # tags = jieba.analyse.extract_tags('我来到北京清华大学')
    # print(list(seg_list_iterator))
    # print(list(tags))
    # # read_url = '/home/jxxiangwen/Downloads/deeplearn/wiki.zh.text_without_doc.utf-8'
    read_url = '/home/jxxiangwen/Downloads/deeplearn/wiki.zh.text_with_blank.utf-8'
    write_url = '/home/jxxiangwen/Downloads/deeplearn/wiki.zh.segment.utf-8'

    with open(write_url, 'w') as write_file:
        with open(read_url) as read_file:
            for line in read_file:
                if len(line) < 1:
                    continue
                seg_list_iterator = jieba.analyse.extract_tags(line)  # 默认是精确模式
                seg_list = list(seg_list_iterator)
                if len(seg_list) < 2:
                    continue
                for element in seg_list:
                    if str.isdigit(element):
                        # print(element)
                        seg_list.remove(element)
                write_file.write(" ".join(seg_list) + '\n')
