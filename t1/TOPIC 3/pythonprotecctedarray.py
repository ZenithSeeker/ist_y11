#THiNGS
password = "1234"
numofguesses = 3
arraylen = 5




def main():
    if passwordcheck(password, numofguesses):
        array = writearray(arraylen)
        displayarray(array)
        sumarray(array)


def displayarray(thisarray):
    [print(i) for i in thisarray]


def writearray(length):
    array = [""] * length
    for i in range(length):
        array[i] = int(input(f"Please enter number {i + 1}:"))
    return array


def sumarray(array):
    total = 0
    for i in array:
        total += i
    print(f"This sum of this array's contents is {total}")


def passwordcheck(password, guessnum):
    verify = False
    guess = input("Enter password here: ")
    while verify == False and guessnum > 0:
        if guess == password:
            verify = True
        else:
            guessnum -= 1
            print(f"{guessnum} tries left")
            guess = input("Retry here: ")

    if not verify:
        print("Ending")
    return verify


main()
