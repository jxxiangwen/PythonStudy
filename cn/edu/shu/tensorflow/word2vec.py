import logging
import os.path
import sys
import multiprocessing

# from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    # program = os.path.basename(sys.argv[0])
    # logger = logging.getLogger("word2vec.py")
    #
    # logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    # logging.root.setLevel(level=logging.INFO)
    # logger.info("running %s" % ' '.join(sys.argv))
    #
    # # check and process input arguments
    # # if len(sys.argv) < 4:
    # #     print(globals()['__doc__'] % locals())
    # #     sys.exit(1)
    # # inp, outp1, outp2 = sys.argv[1:4]
    # inp = '/home/jxxiangwen/Downloads/deeplearn/wiki.zh.segment.utf-8'
    # outp1 = '/home/jxxiangwen/Downloads/deeplearn/wiki.zh.text.model'
    # outp2 = '/home/jxxiangwen/Downloads/deeplearn/wiki.zh.text.vector'
    #
    # model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=1,
    #                  workers=multiprocessing.cpu_count())
    #
    # # trim unneeded model memory = use(much) less RAM
    # # model.init_sims(replace=True)
    # model.save(outp1)
    # model.save_word2vec_format(outp2, binary=False)
    model = Word2Vec.load_word2vec_format('/home/jxxiangwen/Downloads/deeplearn/wiki.zh.text.vector', binary=False)  # C binary format
    model.similarity('男人', '女人')
    model.most_similar(positive=['北京'])
    print(model.similarity('男人', '女人'))
    print(model.most_similar(positive=['北京']))
