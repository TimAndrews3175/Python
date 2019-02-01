#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:41:28 2018

@author: tandrews

Description:
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate message to the user. Hint: how does an 
    even / odd number react differently when divided by 2?

Extras:

1.  If the number is a multiple of 4, print out a different message.
2.  Ask the user for two numbers: one number to check (call it num) 
    and one number to divide by (check). If check divides evenly into num, 
    tell that to the user. If not, print a different appropriate message.
"""
number = int(input("Enter a number: "))

# Print whether the number is even or odd
even = (number % 2) == 0
if even :
    print("%d is even" % number)
else:
    print("%d is odd" % number)

# Extra 1
# Print whether the number is a multiple of 4
multiple_4 = (number % 4) == 0
if multiple_4 :
    print("%d is a multiple of 4" % number)
else:
    print("%d is ***NOT*** a multiple of 4" % number)
    
# Extra 2
# general check to see if a number is a multiple of another number
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if (number1 % number2) == 0 :
    print("{} is a multiple of {}".format(number1, number2))
else:
    print("{} is NOT a multiple of {}".format(number1, number2))