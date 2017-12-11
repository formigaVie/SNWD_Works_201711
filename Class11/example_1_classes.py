#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class human(object):
    def __init__(self, age, name):
        """

        :type age: int
        :type name: str
        """
        self.age = age
        self.name = name

if __name__ == '__main__':
    alfred = human(19, "alfred")
    print alfred.age # access attributes with "."
    print alfred.name