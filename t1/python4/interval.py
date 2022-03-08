# is in rang3 10 -100 ?

def interval():
    number = int(input("Enter a whole number: "))

    if number >= 10 and number <= 100:
        print(str(number) + " is within the interval 10 ... 100")
    else:
        print(str(number) + " is outside the interval 10 ... 100")
interval()
        