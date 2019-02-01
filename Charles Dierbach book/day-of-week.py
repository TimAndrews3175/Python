#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:00:13 2018

@author: tandrews

# Description: 
    For a given month, day, and year, determine the day of the week
    
    Note that that only seems to function correctly going back to 1800.
    
"""
###############################################################
# This script uses Zeller's Rule, which can be found in the following URLs:
# http://www.quickermaths.com/zellers-rule/
# https://en.wikipedia.org/wiki/Zeller%27s_congruence
# https://www.careeranna.com/articles/find-day-for-given-date-quickly/

input_month = int(input("Month: "))
while not int(input_month) in range(1, 13):
    input_month = input("Out of allowed range 1 - 12. Please enter a valid number: ")

input_day = int(input("Day: "))
while not int(input_day) in range(1, 32):
        input_day = input(
           "Out of allowed range 1 - 31. Please enter a valid number: ")

input_year = int(input("Year: "))
while not int(input_year) > 0 :
    year = input(
        "Yeasrs cannot be negative.  Please enter a valid year:  ")

if input_month == 1 or input_month == 2:
    input_month += 12
    input_year -= 1 

if input_month == 1 or input_month == 2:
    input_month += 12
    input_year -= 1 

day_of_week = ( input_day + 13 * (input_month+1) // 5 + input_year + \
               input_year // 4 - input_year// 100 + input_year // 400 ) % 7

days_of_week = {0: "Saturday",1: "Sunday", 2: "Monday",3: "Tuesday",4: 
     "Wednesday",5: "Thursday",6: "Friday"}

print("The day is " + days_of_week[int(day_of_week)] + ".")