#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:59:08 2018

@author: tandrews

Description:
    Return the user's age in days and seconds
 
Example:
Input : Birth date = 07/09/1996 
        Present date = 07/12/2017
Output : Present Age = Years: 21  Months: 3  Days: 0
t Age = Years: 7  Months: 11  Days: 21
"""

SEC_PER_MINUTE = 60
MINUTE_PER_HOUR = 60
HOUR_PER_DAY = 24
SEC_PER_DAY = SEC_PER_MINUTE * MINUTE_PER_HOUR * HOUR_PER_DAY

import datetime
today = datetime.date.today()
print(today)

birth_date_str = input("When were you born?  ")
(year, month, day) = birth_date_str.split(',')
birth_date_final = datetime.date(int(year), int(month), int(day))

# age in days
age = today - birth_date_final
print('You are %d days old.' % age.days  )

# age in seconds
age_secs = age.days * SEC_PER_DAY
print('You are %d seconds old.' % age_secs)