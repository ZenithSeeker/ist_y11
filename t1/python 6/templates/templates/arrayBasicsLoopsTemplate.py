# ---------------------------------------------------------------------------- #
# Author: 
# Date:                   
# Purpose:   

# Answer questions here

# A. Explain in multiple sentances, how the following code improves the 
#    "basics of array program"
# B. How does the use of loops change the program?
# ---------------------------------------------------------------------------- #

def arrayBasicsLoops():


    animalList = [""] * 5

    for i in range(5):
        animalList[i] = input("Please enter an animal: ")

    for i in range(5):
        print("Animal " + str(i + 1) + " is " + animalList[i])