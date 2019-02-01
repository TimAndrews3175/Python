#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:10:27 2018

@author: tandrews

Description:
    Ask the user for a string and print out whether this string is a 
    palindrome or not. (A palindrome is a string that reads the same 
    forwards and backwards.)
"""
input_string = input("Please enter a string of characters:  ")
if input_string == input_string[::-1]:
    print("That is a palindrome.")
else:
    print("That is not a palindrome")