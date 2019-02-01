#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:00:13 2018

@author: tandrews

# Description: 
    For a given month, day, and year, determine the day of the week
"""
from math import floor

#To determine whether a year is a leap year, follow these steps: 
#1.  If the year is evenly divisible by 4, go to step 2. 
#    Otherwise, go to step 5.
#2.  If the year is evenly divisible by 100, go to step 3. 
#     Otherwise, go to step 4.
#3.  If the year is evenly divisible by 400, go to step 4. 
#     Otherwise, go to step 5.
#4.  The year is a leap year (it has 366 days).
#5.  The year is not a leap year (it has 365 days).
def is_leap_year (year):
    year_int = int(year)    
    if (year_int % 4) == 0 :
       if (year_int % 100) == 0:
           if (year_int % 400) == 0:
               return True
           else:
               return False
       else:
           return True
    else:
        return False

month_choices = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

month = input('month:  ').upper()
day_of_month = int(input('day of month:  '))
year = input('year:  ')



century_digits = int(year[0:2])
year_digits = int(year[2:])
value = year_digits + floor(year_digits / 4)

if century_digits == 18 :
    value += 2
else :
    value += 6

if month == month_choices[0] and not is_leap_year(year):
    value += 1
elif month == month_choices[1] :
    if is_leap_year(year):
        value += 3
    else:
        value += 4
elif month == month_choices[2] or month == month_choices[10]: #MAR or NOV
    value += 4
elif month == month_choices[4] : # MAY
    value += 2
elif month == month_choices[5] : # JUN
    value += 5
elif month == month_choices[7] : # AUG
    value += 3
elif month == month_choices[9] : # OCT
    value += 1
elif month == month_choices[8] or month == month_choices[11] : # SEP or DEC
    value += 6

value = (value + day_of_month) % 7

days_of_week = ['Saturday', 'Sunday', 'Monday', 
                'Tuesday', 'Wednesday', 'Thursday',
                'Friday']
print('That day is a ', days_of_week[value] )