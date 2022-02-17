# Author: Samuel Pitchforth
# Date: 14/2/22
# Purpose: Split inputed integer across multiple lines

def fourDigits():
    # takes a number as a string
    num = input("Number: ")
    # is this indexing?
    for letter in num:
        # loops over each character in the string and prints it
        print(letter)


# just in case
def fourDigitsbutnoindex():
    # takes a number as an int
    num = int(input("Number: "))

    # gets the thousands column
    thousands = int(num / 1000)

    # removes the accessed column
    num -= thousands * 1000

    # gets the hundreds column and removes it
    hundreds = int(num / 100)
    num -= hundreds * 100

    # gets the tens column and removes it
    tens = int(num / 10)
    num -= tens * 10

    # ones are here
    ones = int(num)

    # print the collected data
    print(thousands)
    print(hundreds)
    print(tens)
    print(ones)


# fourDigits()
fourDigitsbutnoindex()
