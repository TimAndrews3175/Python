#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:34:23 2018

@author: tandrews

Description:  Various programming exercises from Chapter 2
"""


#P1.  Write a program that prompts the user for 2 int values,
#    and displays the results of the 1st number divided by the 2nd,
#    with exactly 2 decimal places displayed
print('P1')
int1 = int(input('Enter 1st number:  '))
int2 = int(input('Enter 2nd number:  '))
print('The result is %3.2f' % (int1 / float(int2)))


#P2.  Write a program that prompts the user for 2 float values,
#    and displays the results of the 1st number divided by the 2nd,
#    with exactly 6 decimal places displayed
print('P2')
float1 = float(input('Enter 1st float:  '))
float2 = float(input('Enter 2nd float:  '))
print('The 2nd result is %3.6f' % (float1 / float2 ))

# P3.  Prompt for 2 floats and display the result of divining the 1st by the
#   2nd, with exactly 6 decimal places,
#   in scientific notation.
print('P3')
from decimal import Decimal
dec1 = Decimal(input('Enter 1st float:  '))
dec2 = Decimal(input('Enter 2nd float:  '))
x = dec1 / dec2
print('The 3rd result is ', '{:.6e}'.format(x))

# P4.  Prompt user for upper and lower case letters, and display the 
#   corresponding Unicode characters.
print('P4')
char1 = input('Enter 1st char: ')
char2 = input('Enter 2nd char: ')
print('1st char is %s in Unicode' % ord(char1))
print('2nd char is %s in Unicode' % ord(char2))

# P5. Prompt user for 2 integers, and displaythe results of
#   + - * / // % **
print('P5')
int1 = int(input('Enter 1st int'))
int2 = int(input('Enter 2nd int'))
print(int1 , ' + ', int2, '=', (int1 + int2))
print(int1 , ' - ', int2, '=', (int1 - int2))
print(int1 , ' * ', int2, '=', (int1 * int2))
print(int1 , ' / ', int2, '=', (int1 / int2))
print(int1 , ' // ', int2, '=', (int1 // int2))
print(int1 , ' % ', int2, '=', (int1 % int2))
print(int1 , ' * ', int2, '=', (int1 * int2))
print(int1 , ' ** ', int2, '=', (int1 ** int2))