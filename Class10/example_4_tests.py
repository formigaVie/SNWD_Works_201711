#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import example_2_addition_func as CALC

def check_addition():
    assert CALC.addition(10,20)==30
    assert CALC.addition(10,-10)==00

def check_subtraction():
    assert CALC.subtraction(5,-5)==10
    assert CALC.subtraction(10,20)==-10

def check_multiplication():
    assert CALC.multiplication(3,2)==6
    assert CALC.multiplication(4,6)==24

def check_division():
    assert CALC.division(15,3)==5
    assert CALC.division(100,25)==4
    # assert nimmt an das alles was danach kommt Wahr ist - sonst false
    # Assertion error
    # auch für Division by Zero checks

if __name__ == '__main__':
    check_addition()
    print "Passed all addition tests"
    check_subtraction()
    print "Passed all subtraction tests"
    check_multiplication()
    print "Passed all multiplication tests"
    check_division()
    print "Passed all division tests"