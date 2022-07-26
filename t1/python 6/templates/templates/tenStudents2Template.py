# ---------------------------------------------------------------------------- #
# Author: 
# Date:                   
# Purpose:   

# Answer questions here

# 1. based on this program, how many lines of code does it take to read in and
#    print data on 
#   a. 10 students?
#   b. 100 students?
# 2. How has this improved program tenStudents1?
# ---------------------------------------------------------------------------- #


def tenStudents2():
   
   #1. create the array  (1 line of code)
    st = [""] * 10
    for i in range(len(st)):
       st[i] = input("student{}".format(i + 1))
    [print(x) for x in st]

   #2. add data into this array using a loop
   #   (2 lines of code)

   #3. Print a numbered list using a loop
   #   (2 lines of code)
tenStudents2()