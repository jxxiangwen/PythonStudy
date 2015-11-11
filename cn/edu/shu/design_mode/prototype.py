#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'jxxia'

"""
原型模式
"""


class WorkExperience(object):
    def __init__(self, a_place, a_year):
        self.place = a_place
        self.year = a_year


class Resume(object):
    _work_experience = None

    def __init__(self, a_name, a_age):
        self.name = a_name
        self.age = a_age

    def display(self):
        print("我叫{}，{}岁，于{}年在{}学习".format(self.name, self.age, self.work_experience.year, self.work_experience.place))

    @property
    def work_experience(self):
        return self._work_experience

    @work_experience.setter
    def work_experience(self, a_work_experience):
        self._work_experience = a_work_experience

    def clone(self):
        return self


if __name__ == '__main__':
    import copy

    resume = Resume('邹祥文', 24)
    resume.work_experience = WorkExperience('上海大学', 2014)
    resume_clone = resume.clone()
    resume_copy = copy.copy(resume)
    resume_deepcopy = copy.deepcopy(resume)
    resume.age = 21
    resume.work_experience = WorkExperience('上海电力学院', 2009)
    resume_clone.age = 20
    resume_clone.work_experience = WorkExperience('乐平中学', 2005)
    resume_copy.age = 19
    resume_copy.work_experience = WorkExperience('乐平二中', 2002)
    resume_deepcopy.age = 18
    resume_deepcopy.work_experience = WorkExperience('乐平一小', 1997)
    resume.display()
    resume_clone.display()
    resume_copy.display()
    resume_deepcopy.display()
