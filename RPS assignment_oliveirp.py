# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:35:36 2020

@author: Pedro
"""
import numpy as np

while(True):
    player = input("Input 'R' for rock, 'P' for paper, or 'S' for scissors.\nInvalid inputs will result in the computer automatically winning.\n\n")
    player = player.upper()
    print()
    
    computer = np.random.randint(1,3 + 1)
    
    #if computer chooses rock
    if computer == 1:
        computer = 'R'
        print("computer chose rock")
    elif computer == 2:
        computer = 'P'
        print("computer chose paper")
    elif computer == 3:
        computer = 'S'
        print("computer chose scissors")
    
    if computer == player:
        print("the result is a tie")
        print()
        print("do you want to play again? (y/n)")
        print()
    elif (player == 'P' and computer == 'R') or (player == 'R' and computer =='S') or (player == 'S' and computer == 'P') :
        print("the player has won")
        print()
        print("do you want to play again? (y/n)")
        print() 
    else:
        print("the computer has won")
        print()
        print("do you want to play again? (y/n)")
        print()
    again = input("\n\n")
    if again == 'n':
        break
    elif again == 'y':
        pass
    else:
        print("invalid input so it is assumed you want to play again")
    

