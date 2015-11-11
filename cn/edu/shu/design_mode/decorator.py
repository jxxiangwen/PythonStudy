#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'jxxia'

"""
装饰者模式
"""


class Person(object):
    _name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a_name):
        self._name = a_name

    def show(self):
        print('我是{}'.format(self._name))


class Cloth(Person):
    person = None

    def decorator(self, a_person):
        self.person = a_person

    def show(self):
        if self.person:
            self.person.show()


class UnderWear(Cloth):
    def __init__(self):
        pass

    def show(self):
        if self.person:
            self.person.show()
        print('穿上内裤')


class Shirt(Cloth):
    def __init__(self):
        pass

    def show(self):
        if self.person:
            self.person.show()
        print('穿上衬衫')


class Trouser(Cloth):
    def __init__(self):
        pass

    def show(self):
        if self.person:
            self.person.show()
        print('穿上裤子')


class Shoe(Cloth):
    def __init__(self):
        pass

    def show(self):
        if self.person:
            self.person.show()
        print('穿上鞋子')


if __name__ == '__main__':
    person = Person()
    person.name = '邹祥文'
    underWear = UnderWear()
    shirt = Shirt()
    shoe = Shoe()

    underWear.decorator(person)
    shirt.decorator(underWear)
    shoe.decorator(shirt)
    shoe.show()
