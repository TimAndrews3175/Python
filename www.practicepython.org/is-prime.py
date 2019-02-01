#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:53:20 2018

@author: tandrews

@description:
https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no 
divisors.). You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
"""

################################################################
# This is my method.
def is_prime_1 (n):
    if n <= 3:
        return n > 1
    for x in range(2,number-1):
        if (number % x) == 0 :
            return False
    return True
        
###############################################################
# This method is from Wikipedia
# https://en.wikipedia.org/wiki/Primality_test
# updated pseudocode into python
def is_prime_2 (n):
    if n <= 3:
         return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input('Enter a number: '))
print('Testing using my own method...')
print('Is the number prime? ', is_prime_1(number))

print("Testing using Wikipedia's method...")
print('Is the number prime? ', is_prime_2(number))