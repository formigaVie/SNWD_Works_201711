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

    def getolder(self):
        self.age += 1 # self.age = self.age + 1

    def getyounger(self):
        self.age -= 2

    def greet1(self):
        return "Hello, my name is "+self.name+" and i am " + str(self.age)+ "."

    def greet2(self):
        print "Hello, my name is really "+self.name

if __name__ == '__main__':
    alfred = human(19, "alfred")
    print alfred.age # access attributes with "."
    print alfred.name
    alfred.getolder()
    print alfred.age
    print alfred.name
    alfred.getyounger()
    print alfred.age
    #alfred.greet()
    print alfred.greet1()
    alfred.greet2()

