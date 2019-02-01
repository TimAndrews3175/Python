#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:24:24 2018

@author: tandrews

Description
    Take a list, say for example this one:
       a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list that are 
    less than 5.
    
    Extras:
    
    1.  Instead of printing the elements one by one, make a new list that has 
    all the elements less than 5 from this list in it and print out this 
    new list.
    2.  Write this in one line of Python.
    3.  Ask the user for a number and return a list that contains only 
    elements from the original list a that are smaller than that number 
    given by the user.
"""
#numbers = [int(x) for x in input("Enter your numbers:").split()]
#numbers = list(map(int, input().split()))
#print(numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("These are the numbers less than 5:")
for number in numbers:
    if number < 5:
        print(number)
        
#Extra 1:
print("Solution 2:")
new_list = []
for number in numbers:
    if number < 5:
        new_list.append(number)
print(new_list)

#Extra 2:
print("Solution 3:")
max = int(input("What is the max number? "))
new_list = []
for number in numbers:
    if number < max:
        new_list.append(number)
print(new_list)