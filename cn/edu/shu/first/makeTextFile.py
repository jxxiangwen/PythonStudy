# coding=utf-8
__author__ = '祥文'

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

fileName = raw_input("请输入要创建的完整文件名：")
fileName = fileName.encode('gbk')
while True:
    if os.path.exists(fileName):
        fileName = raw_input("文件已存在，请重新输入：")
    else:
        break

content = []
while True:
    temp = raw_input("请输入要填入的信息：")
    if temp == '.':
        break
    else:
        content.append(temp)

newFile = open(fileName, 'w')

newFile.writelines(content)
newFile.close()
