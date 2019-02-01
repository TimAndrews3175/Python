#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:31:20 2018

@author: tandrews
"""
# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
# Take two lists, say for example these two:
# 
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements 
# that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. 
# Write this in one line of Python using at least one list comprehension. 

string_a = input('Enter a list of items, separated by spaces:  ')
list_a = string_a.split(' ')
string_b = input('Enter another list in the same format:  ')
list_b = string_b.split(' ')

list_overlap = [x for x in list_a if x in list_b]
print('The items that are in both lists are: ', list_overlap)