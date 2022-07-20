# ------------------------------------------------------------------------------#
#  Program Name Standard Algorithms - coding task
# -------------------------------------------------
#  Purpose: This program tests the implementation of the load, print and
#           sum array standard algorithms
#  Author:
#  Date:
# ------------------------------------------------------------------------------#


# ------------------------------------------------------------------------------#
#  DO NOT CHANGE MAIN! (except if you need to test)
# ------------------------------------------------------------------------------#
def main():
    element = []

    numElements = loadArray(element)  # adds data to array
    printArrayContents(element, numElements)  # prints data in array
    sumArrayContents(element, numElements)  # sums data in array


#  ADD CODE BELOW
# The functions you will write are below - add 1 in at a time


# ------------------------------------------------------------------------------#
# STUB OF loadArray SUBPROGRAM
#
#  loadArray(element)
# --------------------------------------
#  Purpose:      load data items into array 'element'
#  Parameters:   element:       array to add data item to
#  return:       numElements:   number of items in array
# ------------------------------------------------------------------------------#
def loadArray(element):
    num = int(input("New Value: "))
    while num != -1:
        element.append(num)
        num = int(input("New Value: "))
    print(f"There are {len(element)} items loaded into the array")


# ------------------------------------------------------------------------------#
# STUB OF printArrayContents SUBPROGRAM
#
#  printArrayContents(element,numElements)
# --------------------------------------
#  Purpose:      print data items in the array 'element'
#  Parameters:   element:       array to add data item to
#                numElements:   number of items in array
# ------------------------------------------------------------------------------#
def printArrayContents(element):
    [print(i) for i in element]


# ------------------------------------------------------------------------------#
# STUB OF printArrayContents SUBPROGRAM
#
#  sumArrayContents(element, numElements)
# --------------------------------------
#  Purpose:      sums all items in element array
#  Parameters:   element:       array to add data item to
#                numElements:   number of items in array
# ------------------------------------------------------------------------------#
def sumArrayContents(element):
    total = 0
    for number in element: total += number
    print(f"The sum of the list is {total}")


eee = []
loadArray(eee)
printArrayContents(eee)
sumArrayContents(eee)
