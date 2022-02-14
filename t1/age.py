#Samuel Pitchforth
#9/2/22
#greeting based on

def age():
    # takes full name input
    firstName = input("Please enter your first name: ")
    surname = input("Please enter your surname: ")

    #age input
    age = int(input("Please enter your age: "))

    #newlines
    print("\n\n")

    #Greeting by firstname
    print("Hello " + firstName + " nice to meet you!")

    #tells them their age
    print("You are " + str(age) + " years old " + firstName + ",")

    # Vote calculation
    print("That means you can vote in " + str(18-age) + " years")
    #Goodbye
    print("Goodbye " + firstName + " " + surname)
