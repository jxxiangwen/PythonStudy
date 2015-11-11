#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'jxxia'

"""
工厂方法模式
"""


class LeiFeng(object):
    @staticmethod
    def buy():
        pass


class ClassMate(LeiFeng):
    @staticmethod
    def buy():
        print("大学生学习雷锋买东西")


class Volunteer(LeiFeng):
    @staticmethod
    def buy():
        print("志愿者学习雷锋买东西")


class LeiFengFactory(object):
    @staticmethod
    def create_lei_feng():
        pass


class ClassMateLeiFengFactory(LeiFengFactory):
    @staticmethod
    def create_lei_feng():
        return ClassMate()


class VolunteerLeiFengFactory(LeiFengFactory):
    @staticmethod
    def create_lei_feng():
        return Volunteer()


if __name__ == '__main__':
    lei_feng_factory = ClassMateLeiFengFactory()
    lei_feng = lei_feng_factory.create_lei_feng()
    lei_feng.buy()
    lei_feng_factory1 = VolunteerLeiFengFactory()
    lei_feng1 = lei_feng_factory1.create_lei_feng()
    lei_feng1.buy()