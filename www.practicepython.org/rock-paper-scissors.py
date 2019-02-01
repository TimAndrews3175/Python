#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 21:23:23 2018

@author: tandrews

Description:
    This is taken from
    https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

    Make a two-player Rock-Paper-Scissors game.
    (Hint: Ask for player plays (using input), 
    compare them, 
    print out a message of congratulations to the winner, 
    and ask if the players want to start a new game)

    Remember the rules:

        Rock beats scissors
        Scissors beats paper
        Paper beats rock
"""
def validate_choice (choice_str):
    valid_choices = ['rock', 'paper', 'scissors']
    if any(choice_str in s for s in valid_choices):
        return True
    else:
        return False
    
    
print("Welcome to Rock, Paper, Scissors")
play_again = 'yes'
while (play_again == 'yes'):
    player1 = input("Player 1 choose: ")
    if validate_choice(player1) == False:
        player1 = input('Bad choice.  Enter another string:  ')
    
    player2 = input("Player 2 choose: ")
    if validate_choice(player2) == False:
        player2 = input('Bad choice.  Enter another string:  ')
        
    if player1 == player2 :
        print("Both players chose the same thing.")
    elif player1 == 'rock': 
        if player2 == 'paper': # paper covers rock
             print('Player 2 is the winner')
        else:  #player2 == scissors, rock crushes scissors
             print('Player 1 is the winner')
    elif player1 == 'paper':
         if player2 == 'rock': #paper covers rock
             print ('Player 1 is the winner')
         else: #player2 == scissors , scissors cuts paper
             print('Player 2 is the winner')
    else:  #player 1 == scissors
         if player2 == 'rock':
             print('Player 2 is the winner')
         else : # player2 == paper, scissors cuts paper
             print('Player 1 is the winner')
             
    play_again = input('Do you want to play again? yes/no:  ')
