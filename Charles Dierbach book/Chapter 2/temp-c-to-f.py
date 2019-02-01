#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:31:47 2018

@author: tandrews

Description:
    Convert Celsius to Fahrenheit
"""

print('This program will convert degrees Celsius to degrees Fahrenheit.')

print('Enter degrees Celsius : ')
c_str = input()
c_num = float(c_str)
c_str = '%3.2f' % c_num

# 1.8 * c = f - 32
f_num = (1.8 * c_num) + 32
f_str = '%3.2f' % f_num

print(c_str, 'degrees C = ', f_str, 'degrees F' )