# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:47:41 2019

@author: tsharris
"""
import random
answer = random.randint(1,10)
wallet = 100
print("You have $", wallet)
print()
print("You get 3 tries.")
bet = int ( input("Place your bet:"))
attempts = 3

while (bet>wallet or bet<=0):
        print("Invalid bet amount")
        bet = int ( input("Place your bet:"))
        
while(attempts < 4 ):
    guess = int (input("Guess btwn 1-10:"))
    #print("------------------------------")
    #print("You have $", wallet)
    #answer = random.randint(1,10)
    
    #bet = int ( input("Place your bet:"))
    #check for valid bet amount
    #while (bet>wallet or bet<=0):
        #print("Invalid bet amount")
        #bet = int ( input("Place your bet:"))

    #get user guess
    #guess = int ( input("Guess btwn 1-10:"))
    while (guess < 1 or guess > 10):
        print("Invalid guess")
        guess = int ( input("Guess btwn 1-10:"))

        
    #check guess, update wallet amount
    
    if (attempts == 1):
        wallet = wallet - bet
        print ("Wrong! The answer was", answer)
        print ("You have $", wallet)
        print("No more attempts. Thanks for playing, and thanks for your money.")
        break
    elif (answer != guess):
        attempts = attempts - 1
        print("Try again.", attempts, "left.")
        
    else:
        print ("Correct!")
        wallet = wallet + bet
        break
    
        
    
        
        
            
#else:
            #print ("Wrong! The answer was", answer)
            #wallet = wallet - bet
    #wallet = wallet - bet
    #print ("Wrong! The answer was", answer)
    #print ("You have $", wallet)
    #print("No more attempts. Thanks for playing, and thanks for your money")    