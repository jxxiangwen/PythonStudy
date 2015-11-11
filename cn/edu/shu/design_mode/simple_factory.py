#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'jxxia'

"""
    简单工厂模式
"""


class Operation(object):
    def get_result(self, num1, num2):
        pass


class AddOperation(Operation):
    def get_result(self, num1, num2):
        return num1 + num2


class SubOperation(Operation):
    def get_result(self, num1, num2):
        return num1 - num2


class MulOperation(Operation):
    def get_result(self, num1, num2):
        return num1 * num2


class DivOperation(Operation):
    def get_result(self, num1, num2):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return 0
        return result


class OperationFactory(object):
    def __init__(self, ):
        self.operation = dict()
        self.operation['+'] = AddOperation()
        self.operation['-'] = SubOperation()
        self.operation['*'] = MulOperation()
        self.operation['/'] = DivOperation()

    def create_operation(self, operation):
        return self.operation[operation]


if __name__ == '__main__':
    print(OperationFactory().create_operation('+').get_result(1, 2))
    print(OperationFactory().create_operation('/').get_result(1, 0))
    assert (OperationFactory().create_operation('+').get_result(1, 2) == 3)
