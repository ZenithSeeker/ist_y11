# ---------------------------------------------------------------------------- #
# Author: 
# Date:                   
# Purpose:   

# Answer questions here
# This program uses a concept called parallel arrays.  

# 1. Using your textbook, the internet and your own knowledge,
#    explain what a parallel array is
# 2. Explain the use of the index i in these parallel arrays,
#    specifically with reference to each separate array when
#    at the same index location.
#     e.g. firstName[0], surname[0], age[0]
# ---------------------------------------------------------------------------- #
import numpy as np

def tenStudents3():
    fname = [""] * 10
    lname = [""] * 10
    age = [""] * 10
    for i in range(len(fname)):
        fname[i] = input("First name: ")
        lname[i] = input("Last name: ")
        age[i] = input("Age: ")


    print(fname,lname,age)



tenStudents3()