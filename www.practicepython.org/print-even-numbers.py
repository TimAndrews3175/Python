#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:04:57 2018

@author: tandrews

Description:
    Let’s say I give you a list saved in a variable: 
        a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
    Write one line of Python that takes this list a and makes a new list 
    that has only the even elements of this list in it.

"""

print("Enter a list of numbers")
a = [int(x) for x in input().split()]
even = [x for x in a if x % 2 ==0 ]
all_items = [x for x in a ]
print(all_items)
print("The even numbers are:  ", even)