# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:14:12 2023

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

print("You walk up to the first pressure plate.")

selection=True
#decision=True
active=True
coinselect=""

def coinchoice():
    selection=True
    while selection==True:    
        coinselect=input("Which coin do you wish to place on this plate? ")
        if coinselect !="Quarter" or coinselect !="quarter" or coinselect !="Nickel" or coinselect !="nickel" or coinselect !="Penny" or coinselect !="penny":
                print("Please input either Quarter, Nickel, or Penny.")
                selection=True
        if coinselect=="Quarter" or coinselect=="quarter":
                selection=False
                print("You place a quarter on the plate.")
                selection=False
        if coinselect=="Nickel" or coinselect=="nickel":
                selection=False
        if coinselect=="Penny" or coinselect=="penny":
                selection=False
    return selection
    return coinselect

#player hears knocking if incorrect coin is selected OR plate was equal to 0 meaning it was a dud.
def stepchoice():
    selection=False
    active=True
    while active==True and selection==False:
        if plate1 >= 7 and coinselect !="quarter" or "Quarter":
            print("You hear a slight knocking noise.")
            step=input("Do you wish to proceed? ")
            if step!="Yes" or "yes" or "No" or "no":
                print("Please input Yes or No.")
            if step=="Yes" or step=="yes":
                print("You have stepped on a trap, you have met an untimely demise.")
                break
            if step=="No" or step=="no":
                print("You begin to rethink your decision.")
                selection=True
                coinchoice()
        elif plate1 >= 5 and coinselect !="nickel" or "Nickel":
            print("You hear a slight knocking noise.")
            step=input("Do you wish to proceed? ")
            if step!="Yes" or "yes" or "No" or "no":
                print("Please input Yes or No.")
            if step=="Yes" or step=="yes":
                print("You have stepped on a trap, you have met an untimely demise.")
                break
            if step=="No" or step=="no":
                print("You begin to rethink your decision.")
                selection=True
                coinchoice()
        elif plate1 >= 5 and coinselect !="penny" or "Penny":
            print("You hear a slight knocking noise.")
            step=input("Do you wish to proceed? ")
            if step!="Yes" or "yes" or "No" or "no":
                print("Please input Yes or No.")
            if step=="Yes" or step=="yes":
                print("You have stepped on a trap, you have met an untimely demise.")
                break
            if step=="No" or step=="no":
                print("You begin to rethink your decision.")
                selection=True
                coinchoice()
                return selection


if selection==True:
    coinchoice()
if selection==False:
    print()
    print(f"You place a {coinselect} on the plate")
    stepchoice()



        
    

"""if plate1 >= 7 and coinselect !="quarter" or "Quarter":
    active=True
    print("You hear a slight knocking noise.")
    while decision==True:
        step=input("Do you wish to proceed?")
        if step=="Yes" or step=="yes":
            print("You have stepped on a trap, you have met an untimely demise.")
        if step=="No" or step=="no":
            print("You begin to rethink your decision.")
elif plate1 >= 5 and coinselect !="Nickel" or "nickel":
    active=True
    print("You hear a slight knocking noise.")
    while decision==True:
        step=input("Do you wish to proceed?")
        if step=="Yes" or step=="yes":
            print("You have stepped on a trap, you have met an untimely demise.")
        if step=="No" or step=="no":
            print("You begin to rethink your decision.")
elif plate1 >= 1 and coinselect !="Penny" or "penny":
    active=True
    print("You hear a slight knocking noise.")
    while decision==True:
        step=input("Do you wish to proceed?")
        if step=="Yes" or step=="yes":
            print("You have stepped on a trap, you have met an untimely demise.")
        if step=="No" or step=="no":
            print("You begin to rethink your decision.")"""



























