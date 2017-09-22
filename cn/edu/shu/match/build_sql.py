#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:50:50 2015

@author: 祥文
"""

import pymysql, json
import logging
from time import strftime, localtime

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=('log/build_sql_%s.log' % strftime('%Y-%m-%d', localtime())),
                    filemode='a')


class MsSql:
    """
    对pymysql的简单封装
    pymysql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymysql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：
    """

    def __init__(self):
        with open('./config/database.json', encoding='utf-8') as f:
            json_data = json.load(f)
            self.host = json_data['host']
            self.user = json_data['user']
            self.password = json_data['password']
            self.database = json_data['database']

    def __get_connect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.database:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                    charset="utf8")
        cursor = self.conn.cursor()
        if not cursor:
            raise (NameError, "连接数据库失败")
        else:
            return cursor

    def exec_search(self, sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",password="123456",database="PythonWeiboStatistics")
                resList = ms.exec_search("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cursor = self.__get_connect()
        cursor.execute(sql)
        res_list = cursor.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return res_list

    def exec_non_search(self, sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__get_connect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cursor = self.__get_connect()
        cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

        def exec_continue_search(self, sql):
            """
            执行持续查询语句
            需要手动关闭连接
            返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

            调用示例：
                    ms = MSSQL(host="localhost",user="sa",password="123456",database="PythonWeiboStatistics")
                    resList = ms.exec_search("SELECT id,NickName FROM WeiBoUser")
                    for (id,NickName) in resList:
                        print str(id),NickName
            :param sql: 查询语句sql代码
            :return:
            """
            cursor = self.__get_connect()
            # print(cursor)
            cursor.execute(sql)
            res_list = cursor.fetchall()
            return res_list

        def exec_continue_non_search(self, sql):
            """
            执行持续非查询语句
            需要手动关闭连接
            调用示例：
                cur = self.__get_connect()
                cur.execute(sql)
                self.conn.commit()
                self.conn.close()
            :param sql: 非查询语句sql代码
            :return:
            """
            cursor = self.__get_connect()
            cursor.execute(sql)
            self.conn.commit()


if __name__ == '__main__':
    # 创建一个数据库对象
    sql = MsSql()
    user_key_result = sql.exec_search("select * from UserKeyWdsInfor")
    if not user_key_result:
        print("user_key_result", user_key_result)
    # 取出所有记录，返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    for (UserInfor_ID, UserInfor_Birth) in user_key_result:
        print("UserInfor_ID:" + str(UserInfor_ID) + ",UserInfor_Birth:" + UserInfor_Birth + "")
        # sql.exec_non_search("update UserInfor set UserInfor_Birth='1991-07-25' where UserInfor_ID=1")
