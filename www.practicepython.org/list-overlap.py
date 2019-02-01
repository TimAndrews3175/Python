#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 08:45:58 2018

@author: tandrews

Description:
    Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements 
    that are common between the lists (without duplicates). 
    Make sure your program works on two lists of different sizes.

    Extras:
    
    Randomly generate two lists to test this
    Write this in one line of Python 
    (don’t worry if you can’t figure this out at this point - 
    we’ll get to it soon)
"""
print("Enter the 1st list without any brackets or commas")
list1 = [int(x) for x in input().split()]
print("The 1st list is : " , list1)

print("Enter the 2nd list in the same format")
list2 = [int(x) for x in input().split()]
print("The 2nd list is : " , list2)

common_elements = []
for x in list1:
    if x in list2:
        common_elements.append(x)
        
print("The common elements are: ", common_elements)