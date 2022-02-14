#Author: Samuel Pitchforth
#Date: 14/2/22
#Purpose: The sum of the digits of a 5 digit number (lists are indexed right)

def notfourdigits():
    num = int(input("Number: "))

    #gets the ten thousands column

    tentho = int(num /10000)
    num -= tentho * 10000

     #gets the thousands column
    thousands = int(num /1000)

    #removes the accessed column
    num -= thousands * 1000

    #gets the hundreds column and removes it
    hundreds = int(num /100)
    num -= hundreds * 100

    #gets the tens column and removes it
    tens = int(num /10)
    num -= tens * 10

    #ones are here
    ones = int(num)

    print("Sum: " + str(tentho + thousands + hundreds + tens + ones))



notfourdigits()
