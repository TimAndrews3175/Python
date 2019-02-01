#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:04:53 2018

@author: tandrews

Description:
    Create a program that asks the user to enter their name and their age. 
    Print out a message addressed to them that tells them the year that 
    they will turn 100 years old.

Extras:

1.  Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message. 
    (Hint: order of operations exists in Python)
2.  Print out that many copies of the previous message on separate lines. 
    (Hint: the string "\n is the same as pressing the ENTER button)
"""
from time import gmtime # tm_year

name = input("Please enter your name: ")
age = int(input("How old are you?  "))

years_before_100 = 100 - age

age_at_100 = gmtime().tm_year + years_before_100

print(name)

#message = "You will be 100 years old in " + str(years_before_100) + \
#    " years in " + str(age_at_100) + "."
message =  "You will be 100 years old in %d years in %d" % (years_before_100, age_at_100)
print(message)     

#Extra 1 + 2:
number = int(input("Enter a number of repititions: "))
print((message + "\n") * number)

