# ---------------------------------------------------------------------------- #
# Author: 
# Date:                   
# Purpose:   
# ---------------------------------------------------------------------------- #
# Answer questions here
# ---------------------
# The following is a line of code from the program below.  
#     animalList[0] = "Frog"
#
# a. What value is in animalList[0] before the above line is run?
# b. What value is in animalList[0] after the above line is run?
# ---------------------------------------------------------------------------- #
 
def arrayBasics():

   #declares an array called animallist with 5 values
   ## ADD A LINE OF CODE HERE
   animalList = [""] * 5



   #to add data into this array
   animalList[0] = "Frog"
   animalList[1] = "COw"
   animalList[2] = "Dog"
   animalList[3] = "Cat"
   animalList[4] = "Bird"
   ## ADD 4 LINES OF CODE HERE

   print("The value of the array with your own data are")
   print("The first element stored in the array is " + animalList[0])
   print("The second element stored in the array is " + animalList[1])
   print("The third element stored in the array is " + animalList[2])
   print("The fourth element stored in the array is " + animalList[3])
   print("The fifth element stored in the array is " + animalList[4])

   animalList[0] = input("Enter first animal name: ")
   animalList[1] = input("Enter second animal name: ")
   animalList[2] = input("Enter third animal name: ")
   animalList[3] = input("Enter fourth animal name: ")
   animalList[4] = input("Enter fifth animal name: ")

   print("The value of the array with your own data are")
   print("The first element stored in the array is " + animalList[0])
   print("The second element stored in the array is " + animalList[1])
   print("The third element stored in the array is " + animalList[2])
   print("The fourth element stored in the array is " + animalList[3])
   print("The fifth element stored in the array is " + animalList[4])


arrayBasics()
