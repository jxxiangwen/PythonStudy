#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'jxxia'

"""
    策略模式
"""


class Context(object):
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def get_result(self):
        self.algorithm.execute()


class Algorithm(object):
    def execute(self):
        pass


class AlgorithmA(Algorithm):
    def execute(self):
        print("AlgorithmA is executing")


class AlgorithmB(Algorithm):
    def execute(self):
        print("AlgorithmB is executing")


class AlgorithmC(Algorithm):
    def execute(self):
        print("AlgorithmC is executing")


if __name__ == '__main__':
    strategy = list()
    strategy.append(Context(AlgorithmA()))
    strategy.append(Context(AlgorithmB()))
    strategy.append(Context(AlgorithmC()))
    strategy[0].get_result()
    select = input("type:[0]for AlgorithmA,[1]for AlgorithmB [2]AlgorithmC.")
    if int(select) < len(strategy):
        cc = strategy[int(select)]
    else:
        print("Unknown type.Use AlgorithmA mode.")
        cc = strategy[0]
    cc.get_result()
