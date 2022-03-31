# ------------------------------------------------------------------------#
# pattern                                                                 #
# ------------------------------------------------------------------------#
# Purpose: Create patterns of alternating characters, to a specified size #
# Author:Samuel Pitchforth                                                #
# Date: 25/03/2022                                                        #
# ------------------------------------------------------------------------#

def pattern():
    print("- - - - - - - - - - - - - - -")
    print("| Pattern generator")
    print("- - - - - - - - - - - - - - -")
    char_one = input("| Character 1   : ")
    char_two = input("| Character 2   : ")
    num = int(input("| Size of pattern: "))

    while len(char_one) != 1:
        print("|    ---ERROR---")
        print("|   Character 1 must \n"
              "|  be a single character")
        print("")
        print("Re - enter")
        char_one = input("| Character 1   : ")

    while len(char_two) != 1:
        print("|    ---ERROR---")
        print("|   Character 2 must \n"
              "|  be a single character")
        print("")
        print("Re - enter")
        char_two = input("| Character 2   : ")

    while num < 2 or num > 50:
        print("|       ---ERROR---")
        print("|   Number must be within\n"
              "|        range 2-50 ")
        print("")
        print("Re - enter")
        num = int(input("| Size of pattern: "))

    print("- - - - - - - - - - - - - - -\n")


    print("- " * num)

    for y in range(num):
        for x in range(num):
            if (x+y)%2 == 0:
                print(char_one, end=" ")
            else:
                print(char_two, end=" ")
        print()
    print("- " * num)


pattern()