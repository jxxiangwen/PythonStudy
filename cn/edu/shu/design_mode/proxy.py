#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'jxxia'

"""
代理模式
"""


class Subject(object):
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print('RealSubject 求爱')


class Proxy(Subject):
    subject = None

    def request(self):
        if not self.subject:
            self.subject = RealSubject()
        self.subject.request()


if __name__ == '__main__':
    proxy = Proxy()
    proxy.request()
