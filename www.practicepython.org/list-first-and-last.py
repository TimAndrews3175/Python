#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:13:11 2018

@author: tandrews
"""
# Write a program that takes a list of numbers 
#(for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given 
# list. For practice, write this code inside a function.

input_list = input('Enter a list of numbers:  ')
list_integers = list(map(int, input_list))