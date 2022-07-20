def passwordcheck(password, guessnum):
    verify = False
    guess = input("Enter password here: ")
    while not verify and guessnum > 1:
        if guess == password:
            verify = True
        else:
            guessnum -= 1
            print(f"{guessnum} tries left")
            guess = input("Retry here: ")

    if not verify:
        print("Ending")
    return verify

def loaddata():
    with open("pass1.txt", "r") as f:
        return f.readline().strip()

def changepword(npword):
    f = open("pass1.txt", "w")

    f.write(npword)
    f.close()



def main():
    if passwordcheck(loaddata(),3):

        changepword(input("Please put in new password"))
main()
