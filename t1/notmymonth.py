def dateFormat():
    # getting user input for the date
    print("-" * 5)
    print("Enter a date in the following format dd/mm/yyyy")
    print("e.g. 12/08/2022:")
    date = input("Enter date: ")
    print("-" * 5)

    # setting the satisfy count as 0
    # when the count reaches a certain number the code will execute program
    satisfy_count = 0

    # we first set the repeat as yes
    # so that it can go through the while loop
    repeat = "Y"

    while repeat == "Y":

        # if the month is less than 1 (jan) or greater than 12 (dec)
        while int(date[3] + date[4]) < 1 or int(date[3] + date[4]) > 12:
            print(" ")
            print("- - - ERROR - - - -")
            print("invalid month")
            print("- - - - - - - - - -")
            print("Please re-enter month value within range 01-12")
            print(" ")
            print("-" * 5)
            print("Enter a date in the following format dd/mm/yyyy")
            print("e.g. 12/08/2022:")
            date = input("Enter date: ")
        satisfy_count += 1

        # if the user inputs invalid date length
        # we check this by checking the length of the date inputted
        # as it would normally be the length of 10 characters
        while len(date) != 10:
            print(" ")
            print("- - - ERROR - - - -")
            print("invalid date format")
            print("- - - - - - - - - -")
            print("Check the date entry follows the correct format")
            print("dd/mm/yyyy")
            print(" ")
            print("-" * 5)
            print("Enter a date in the following format dd/mm/yyyy")
            print("e.g. 12/08/2022:")
            date = input("Enter date: ")
        satisfy_count += 1

        # if all the error checks have passed
        if satisfy_count == 2:
            # then now we correspond the month inputted to the correct month
            if date[3] == "0" and date[4] == "1":
                month = "January"
            elif date[3] == "0" and date[4] == "2":
                month = "February"
            elif date[3] == "0" and date[4] == "3":
                month = "March"
            elif date[3] == "0" and date[4] == "4":
                month = "April"
            elif date[3] == "0" and date[4] == "5":
                month = "May"
            elif date[3] == "0" and date[4] == "6":
                month = "June"
            elif date[3] == "0" and date[4] == "7":
                month = "July"
            elif date[3] == "0" and date[4] == "8":
                month = "August"
            elif date[3] == "0" and date[4] == "9":
                month = "September"
            elif date[3] == "1" and date[4] == "0":
                month = "October"
            elif date[3] == "1" and date[4] == "1":
                month = "November"
            else:
                month = "December"

                # now we figure out the st, nd, rd, th for the day
            if int(date[0] + date[1]) == "1":
                ending = "st"
            elif int(date[0] + date[1]) == "2":
                ending = "nd"
            elif int(date[0] + date[1]) == "3":
                ending = "rd"
            elif int(date[0] + date[1]) == "21":
                ending = "st"
            elif int(date[0] + date[1]) == "22":
                ending = "nd"
            elif int(date[0] + date[1]) == "23":
                ending = "rd"
            elif int(date[0] + date[1]) == "31":
                ending = "st"
            else:
                ending = "th"

            # now we output the converted date
            # by converting the month to a string
            # now we convert the index 0 and 1 (the day) into a string plus the st or nd etc..
            # then we do the year which is str(date[6]+date[7]+date[8]+date[9]
            print("Date: " + str(month) + " " + str(int(date[0] + date[1])) + ending + ", " + str(
                date[6] + date[7] + date[8] + date[9]))
            print("-" * 5)

            # now we ask the user if they want to repeat the program
            print(" ")
            print("Run the program again (y/n):")
            # we convert the user input into capitalization
            # therefore, if the user types y or Y it will do the same thing
            choice = input("Enter  choice: ").upper()
            print("-----")
            print(" ")

        # if the choice is yes
        # then we set the repeat as yes
        if choice == "Y":
            repeat = "Y"
        else:
            # otherwise we output this message
            repeat = "N"
            print("Bye, Thankyou for using the data formatter")


dateFormat()