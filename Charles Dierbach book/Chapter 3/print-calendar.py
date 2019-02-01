#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:47:40 2018

@author: tandrews

@description:
    Display a calendar month for any given month between
    Jan 1800 and Dec 2099.
    
    The format should be as shown
May 2012

Sun  Mon  Tue  Wed  Thu  Fri  Sat

            1    2    3    4    5
  6    7    8    9   10   11   12
 13   14   15   16   17   18   19
 20   21   22   23   24   25   26
 27   28   29   30   31   
"""

####################################################
# Caclulate 1st day of the month
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
    
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                 'August', 'September', 'October', 'November', 'December']

def first_day_of_month(month, year)
if century_digits == 18 :
    value += 2
else :
    value += 6

if month == MONTHS[0] and not is_leap_year(year):
    value += 1
elif month == MONTHS[1] :
    if is_leap_year(year):
        value += 3
    else:
        value += 4
elif month == MONTHS[2] or month == MONTHS[10]: #MAR or NOV
    value += 4
elif month == MONTHS[4] : # MAY
    value += 2
elif month == MONTHS[5] : # JUN
    value += 5
elif month == MONTHS[7] : # AUG
    value += 3
elif month == MONTHS[9] : # OCT
    value += 1
elif month == MONTHS[8] or month == MONTHS[11] : # SEP or DEC
    value += 6

value = (value + day_of_month) % 7

#####################################################
# Display the calendar month, provided day of the week that it falls on


