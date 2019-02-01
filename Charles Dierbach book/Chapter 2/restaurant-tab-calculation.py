#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:26:08 2018

@author: tandrews

Description:
    Calculate a restaurant tab
    
"""


intro_str = """This program will calculate a restauranttabe fora couple with 
a gift certificate, with a restaurant tax as input
"""
print(intro_str)
rest_tax = float(input('Enter the restaurant tax:  '))

gift_cert_amount = int(input('Enter the amount of the gift certificate:  '))

print('Enter ordered items for person 1. ')
person1_appetizer = float(input('Appetizer: '))
person1_entree = float(input('Entree:'))
person1_drinks = float(input('Drinks:  '))
person1_dessert = float(input('Dessert:  '))

print('Enter ordered items for person 2. ')
person2_appetizer = float(input('Appetizer: '))
person2_entree = float(input('Entree: '))
person2_drinks = float(input('Drinks:  '))
person2_dessert = float(input('Dessert:  '))

items_price = \
    person1_appetizer + person1_entree + \
    person1_drinks + person1_dessert + \
    person2_appetizer + person2_entree + \
    person2_drinks + person2_dessert
print('Ordered items: $ %3.2f' % items_price)    

total_tax = items_price * rest_tax
print('Restaurant tax : $ %3.2f' % total_tax)

tab = float(input('Tab: (negative for gift certificates): '))

total_price = items_price + total_tax + tab
print('Total price %3.2f.' % total_price)
print('A negative amount indicates there is a balance on a gift certificate.')

# Problem M2, page 76
# Display total cost of drinks and deserts, and % of the total of meal
#   (before tax) that these items comprise.
#   Display the monetory amount rounded to 2 decimal places.
total_drinks_dessert = person1_drinks + person1_dessert + \
    person2_drinks + person2_dessert
percent_drinks_dessert = total_drinks_dessert / items_price * 100
print('Drinks and dessert cost ', total_drinks_dessert)
print('That was %d percent of the price.' % percent_drinks_dessert )