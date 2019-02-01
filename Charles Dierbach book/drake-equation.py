#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:11:14 2018

@author: tandrews
Description:
    Calculate the likelyhood of alien life in our galaxy
        based on inputs from the user.
    
    
    #***********************************************************
    ### Variables ###
    Factor Value - symbol - estimated value
    Rate of star creation pe year - R - 7
    
    ### Inputs ###
    Percentage of stars with planets - p - 40%
    Average number of planets that can support life for each star with
        planets - n - ???
    Percentage of planets that can potentially support life - f - 13 %
    Percentage of planets that can support INTELLIGENT life - i - ???
    Percentage of planets that are willing and able to communiicate - c - ???
    Expected lifetime of civilizations - L - ???
    
    N = The number of civilizations in the Milky Way Galaxy whose 
        electromagnetic emissions are detectable.  This is the ultimate answer
        that astrobiologists seek.
    R* = The rate of formation of stars suitable for the development of 
        intelligent life.
    fp = The fraction of those stars with planetary systems.
    ne = The number of planets, per solar system, with an environment 
        suitable for life.
    fl = The fraction of suitable planets on which life actually appears.
    fi = The fraction of life bearing planets on which 
        intelligent life emerges.
    fc = The fraction of civilizations that develop a technology 
        that releases detectable signs of their existence into space.
    L = The length of time such civilizations release detectable 
        signals into space.
    
    N = R* * fp * ne * fl * fi * fc * L

"""
# rate of star creation per year
# This is the only factor for which there is any broad consensus.
# http://www.astrodigital.org/astronomy/drake_equation.html states this 
#   ranges from 5 to 20.
R= 7 


print('Hello. Welcome to the Drake Equation calculator.')
print('Please enter the following inputs.')
fp = float(input('Percentage of stars with planets (fp):  '))
ne = float(input(
    'Number of planets per system with suitable environments (ne):  '))
fl = float(input(
    'Percentage of planets that do support life (fl):  '))
fi = float(input(
    'Percentage of planets that support INTELLIGENT life (fi): '))
fc = float(input(
    'Percentage of planets that are willing and able to communiicate (fc):  '))
l = int(input('Expected lifetime of civilizations (L)'))

answer = int(R * fp * ne * fl * (fi/100) * (fc/100) * l)

print('Based on the formula there are potentially ')
print(answer)
print('planets with intelligent life in our galaxy')