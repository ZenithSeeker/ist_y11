# --------------------------------------------------------------------#
# dateFormat                                                          #
# --------------------------------------------------------------------#
# Purpose: Read in dd/mm/yyyy format and convert to word based format #
# Author:Samuel Pitchforth                                            #
# Date: 25/03/2022                                                    #
# --------------------------------------------------------------------#

def dateFormat():
    loop = True
    while loop:



        ##Makes a horizontal dividing line and gives info to user
        print("-------------------------------------------------------------"
              "---------")
        print("Enter a date in the dd/mm/yyyy format\n"
              "An example of this would be \"16/03/2022\"")
        # gets date in format
        date = input("Enter date:")



        ##checks if input length is 10.
        # If not give an error and request a new input
        while len(date) != 10:
            print("\n!-----ERROR-----!\n"
                  "  Invalid format\n"
                  "-----------------\n \n"
                  "Check your date is in the proper dd/mm/yyyy format")
            print("-------------------------------------------------------------"
                  "---------")
            print("Enter a date in the dd/mm/yyyy format\n"
                  "An example of this would be \"16/03/2022\"")
            # gets date in format
            date = input("Enter date:")

        # gets the 3 and 4 th character of the string that corresponds to the date
        month = int(date[3:5])

        # if the month number is not valid give an error and request a new input
        while month < 1 or month > 12:
            print("\n!-----ERROR-----!\n"
                  "  Invalid Month\n"
                  "-----------------\n \n"
                  "Check your month is between 1 and 12")
            print("-------------------------------------------------------------"
                  "---------")
            print("Enter a date in the dd/mm/yyyy format\n"
                  "An example of this would be \"16/03/2022\"")
            # gets date in format
            date = input("Enter date:")
            month = int(date[3:5])

        year = date[6:10]
        # drops the first digit if it is a zero
        if date[0] == "0":
            day = date[1]
        else:
            day = date[0:2]

        second_digit_of_day = int(date[1])

        ##checks which suffix to use
        if second_digit_of_day == 1 and day != "11":
            suffix = "st"
        elif second_digit_of_day == 2 and day != "12":
            suffix = "nd"
        elif second_digit_of_day == 3 and day != "13":
            suffix = "rd"
        else:
            suffix = "th"

        ##Multiway selection that picks the correct month based on the number
        #input
        if month == 1:
            word_month = "January"
        elif month == 2:
            word_month = "February"
        elif month == 3:
            word_month = "March"
        elif month == 4:
            word_month = "April"
        elif month == 5:
            word_month = "May"
        elif month == 6:
            word_month = "June"
        elif month == 7:
            word_month = "July"
        elif month == 8:
            word_month = "August"
        elif month == 9:
            word_month = "September"
        elif month == 10:
            word_month = "October"
        elif month == 11:
            word_month = "nov"
        else:
            word_month = "dec"
        # prints the month + the day + the suffix and the year together.
        print("-----------------")
        print(word_month + " " + day + suffix + ", " + year)
        print("-----------------\n")
        print("Would you like to rerun the program? (y/n)")

        choice = input("Enter choice: ")
        if choice == "n" or choice == "N":
            loop = False

    print("Goodbye. Thank you for using the date formater.")


dateFormat()
