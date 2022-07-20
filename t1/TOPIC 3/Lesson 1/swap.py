#-------------------------------------------------------------------------------
#   Author:    Your Name
#   Purpose:   What does this program do?
#   date:      DD/MM/YY
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#   Instructions
#-------------------------------------------------------------------------------
#   a. Create the swap program - Template Below
#       This should implement the below pseudocode
#
#    BEGIN MAINPROGRAM
#       Get first from user input
#       Get second from user input
#       swap(first, second)
#    END MAINPROGRAM
#
#    BEGIN SUBPROGRAM swap(item1, item2)
#       temp  = item1
#       item1 = item2
#       item2 = temp
#       Display "First:" item1 "second:" item2
#    END SUBPROGRAM swap

#      --------------------------------------------------------------------------
#   b. Include your own comments explaining each line of processing.
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# The purpose of main()
# is to get the inputs and call swap

def main():
    item1 = input("item1: ")
    item2 = input("item2: ")
    swap(item1, item2)


#-------------------------------------------------------------------------------
# The purpose of swap()swap two variables
# The parameters are -
def swap(item1,item2):
    temp = item1
    item1 = item2
    item2 = temp
    print("FIRST: " + str(item1) + "   SECOND" + str(item2))