#coding=utf-8
__author__ = '祥文'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

fileName = raw_input("请输入要创建的完整文件名：")
fileName = fileName.encode('gbk')
try:
    newFile = open(fileName)
except IOError,error:
    print "文件不存在或权限不够",error
else:
    for line in newFile:
        print line.decode('gbk')

    newFile.close()
