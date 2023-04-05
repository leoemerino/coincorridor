# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:41:54 2023

@author: Leo
"""

intuition="Yes" or "yes"

print("You find your self in a corridor that is one tile wide, you step forward and notice the tile in front of you seems suspicious.")
print()

while intuition == "Yes" or intuition == "yes":
    check=input("Do you wish to examine the tile? ")
    if check != "Yes" or check !="yes" or check !="No" or check !="no":
        intuition="Yes" or intuition =="yes"
        print("Please answer with 'Yes' or 'No'")
    if check=="No" or check =="no":
            print("You step onto the plate and face an untimely demise.")
            print("Goodbye.")
            intuition=="No" or intuition=="no"
            break
    if check=="Yes" or check =="yes":
            print("You have examined the tile, it appears that it is a pressure plate.")
            print()
            print("It seems that something devious is afoot...")
            intuition=="No" or intuition=="no"
            break

