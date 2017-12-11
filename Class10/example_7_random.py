#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random

if __name__ == '__main__':
    numbers = range(20)
    print numbers
    random.shuffle(numbers)
    print numbers