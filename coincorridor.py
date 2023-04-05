# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:31:17 2023

@author: Leo
"""

import random

#plates=random.randint(1,10)
coins=["quarter","nickel","penny"]
plates=[]

for traps in range(10):
    plates.append(random.randint(1,10))
    plates[-1]
    traps=traps+1
    
plate1=plates[0]
plate2=plates[1]
plate3=plates[2]
plate4=plates[3]
plate5=plates[4]
plate6=plates[5]
plate7=plates[6]
plate8=plates[7]
plate9=plates[8]
plate10=plates[9]

def game():
    print()
    print("You step forward sheepishly in the corridor.")
    print("The corridor is single tiled all the way to a door.")
    print("You notice that some tiles are raised.")
    intuition=True

    while intuition==True:
        check=input("Do you wish to examine the tile? ")
        if check=="No" or check =="no":
            print() 
            print("You step onto the plate and face an untimely demise.")
            print("Goodbye.")
            intuition==False
            break
        if check=="Yes" or check =="yes":
            print()
            print("You have examined the tile, it appears that it is a pressure plate.")
            print()
            print("It seems that something devious is afoot...")
            print()
            print("You've seen enough movies to know that the coins and the plates must be connected.")
            print("Something inside of you thinks that placing a coin on the plate may do something.")
            intuition==False
            break
        else:
            print()
            print("Please answer with 'Yes' or 'No'")
            print()
    

    
    
    
    """awareness=input("Do you wish to inspect the raised tile? ")
    if awareness=="no":
        print("Step forward onto the plate and face an untimely death.")
    if awareness=="yes":
        print("These raised tiles seem to be pressure plates!")
        print("Let's not be the ones who find out what happens when one steps on them.")
    else:
        print("Please answer yes or no.")
    print()
    print("Your intuition tells you that you might be able to use your change to disarm the pressure plates.")"""
    
    
        
    

"""if plates >= 7:
    quarter=True
    nickel=False
    penny=False
elif plates >= 3:
    quarter=False
    nickel=True
    penny=False
else:
    quarter=False
    nickel=False
    penny=True"""
    
print("===The Coin Corridor===")
print()
print("You find yourself in a long corridor.")
print("You look behind you and there is only a pale wall cold to the touch.")
print("You seem to have an awful lot of change in your pocket")

game()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    