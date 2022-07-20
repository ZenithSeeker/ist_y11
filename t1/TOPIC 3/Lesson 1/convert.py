#-------------------------------------------------------------------------------
#   Author:    Your Name
#   Purpose:   What does this program do?
#   date:      DD/MM/YY
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#   Instructions
#-------------------------------------------------------------------------------
#   a. Create the modularTempConv program from  - Template Below
#       This should implement the below description
#
#       You have already created a temperature converter last term.
#       Now you will turn this into a subroutine. Given The following,
#
#       Design a program that converts a temperature from Fahrenheit into Celsius.
#
#       Your task it to create the main program.
#       The main program will take in Fahrenheit and use the below function call
#       to call upon the provided function convert
#
#       Function Call:        convert(fht)
#
#       Function:             def convert(tempFht ):
#	                         tempCelsius = (5.0/9.0)*(tempFht - 32);
#	                         return tempCelsius;
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# The purpose of main()
#
def main():
    numb = float(input("Enter temp in Farenheit: "))

    print("Your temp in Celsius is "  + str(convert(numb)))


#-------------------------------------------------------------------------------
# The purpose of convert()
# The parameters are -
def convert(tempFht):
   tempCelsius = (5.0/9.0)*(tempFht - 32);
   return tempCelsius;

