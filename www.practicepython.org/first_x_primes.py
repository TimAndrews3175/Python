#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:09:42 2018

@author: tandrews

@description:  Print the first X prime numbers

"""
def is_prime (n):
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

numbers_to_print = int(input('How many prime numbers do you want to print?  '))

for x in range(1,numbers_to_print):
    if is_prime(x) :
        print (x)
