# -------------------------------------------------------------------------------
#   Author:    Samuel Pitchforth
#   Purpose:   What does this program do?
#   date:      17/05/2020
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
#   Instructions
# -------------------------------------------------------------------------------
#   a. Create the Larger program. - Template Below
#
#      --------------------------------------------------------------------------
#   b. Include your own comments explaining each line of processing.
#      Please pay particular attention to the parts of code which relate
#      to sub programs.
#
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# TCall larger2 with different params
#
def main():
    larger2(1,2)
    larger2(7.5, 9.5)
    larger2(255, 83)
    larger2(1, 2)
    x = 5
    y = 89
    larger2(x, y)
    larger2(y, x)

    one = int(input("Number "))
    two= int(input("Number "))
    print("Largest: " + str(larger(one, two)))

# -------------------------------------------------------------------------------
# The purpose of larger() is to compare the two params and return the larger value
# The parameters are - num1, num2
def larger(num1, num2):
    if num1 > num2:
        largest = num1
    else:
        largest = num2
    return largest


# -------------------------------------------------------------------------------
# The purpose of larger2() is to print the larger value
# The parameters are - num1, num2
def larger2(num1, num2):
    if num1 > num2:
        print(str(num1) + " is larger")
    else:
        print(str(num2) + " is larger")