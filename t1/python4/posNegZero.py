# pos or neg or zero

def posNegZero():
    number = int(input("Enter a whole number: "))
    if number > 0:
        print(str(number) + " is a positive")
    elif number == 0:
        print(str(number) + " is zero")
    else:
        print(str(number) + " is a negative")

posNegZero()