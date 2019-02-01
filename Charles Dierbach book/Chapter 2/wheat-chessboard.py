#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:59:37 2018

@author: tandrews

@description:  Wheat and chessboard problem, displayed in pounds

https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem

With 64 squares on a chessboard, if the number of grains doubles on 
successive squares, then the sum of grains on all 64 squares is: 
    1 + 2 + 4 + 8 + ... and so forth for the 64 squares. 
    The total number of grains equals 18,446,744,073,709,551,615, 
    much higher than most expect.

This exercise can be used to demonstrate how quickly exponential sequences
 grow, as well as to introduce exponents, zero power, 
 capital-sigma notation and geometric series. 
 Updated for modern times using pennies and the hypothetical question, 
 "Would you rather have a million dollars or the sum of a penny doubled 
 every day for a month?", 
 the formula has been used to explain compounded interest.

Page 77, Problem D1

"""
WEIGHT_1_GRAIN = 1.0/7_000
LB_TO_KG = 0.453592

#######################################################################3
# Calculate total number of grains
#brute force method

# 64 squares on a chessboard, so 64 can be a limit
limit = int(input('Enter the upper limit of times to double:  '))
total_grains = 0
for x in range(0,limit): 
    total_grains += 2**x
print('---1st method---')
print('Total # of grains : ', f"{total_grains:,d}")

# better method
total_grains = 2**limit - 1
print('---2nd method---')
print('Total # of grains : ', f"{total_grains:,d}")
      
#######################################################################
# Calculate weight
weight_pounds = total_grains * WEIGHT_1_GRAIN
print('Weight in pounds: ', f"{weight_pounds:,f}")
weight_kg = weight_pounds * LB_TO_KG
print('Weight in kilograms: ', f"{weight_kg:,f}")
      