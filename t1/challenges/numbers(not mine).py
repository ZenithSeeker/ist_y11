
def numbers():

    size = int(input("size: "))

    number = 1

    #increment = 0


    for row in range(size):
        for i in range(number, size + number):
            print(i, end = "  ")

        print(" ")

numbers()