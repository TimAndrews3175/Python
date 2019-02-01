#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 09:52:39 2018

@author: tandrews
"""
from time import localtime
day = localtime().tm_mday
month = localtime().tm_mon
year = localtime().tm_year
print("The current date is %d-%d-%d" %(year, month, day))

hour = localtime().tm_hour
minute = localtime().tm_min
print("The time is %d:%d" % (hour, minute))

