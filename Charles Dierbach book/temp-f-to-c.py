#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:31:47 2018

@author: tandrews

Description:
    Convert Fahrenheitt0 Celsius
"""

print('This program will convert degrees Fahrenheit to degrees Celsius.')

print('Enter degrees Fahrenheit : ')
f_str = input()
f_num = float(f_str)
f_str = '%3.2f' % f_num

# 1.8 * c = f - 32
c_num = (f_num - 32) / 1.8
c_str = '%3.2f' % c_num

print(f_str, 'degrees F = ', c_str, 'degrees C' )