#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:10:51 2018

@author: tandrews

Description:
    Create a program that asks the user for a number and then prints out a 
    list of all the divisors of that number. (If you don’t know what a divisor
    is, it is a number that divides evenly into another number. For example, 
    13 is a divisor of 26 because 26 / 13 has no remainder.)

"""
input_number = int(input("Enter a number: "))
print("Here are the divisors of ", input_number)
for x in range(1, input_number+1):
    if (input_number % x) == 0 :
        print(x)
