from pass1 import passwordcheck

def findpword(uname):
    with open("pass4.txt", "r") as f:
        line = f.readline().strip()
        while line != "ZZZ":
            if line.split()[0] == uname:
                return line.split()[1]
            line = f.readline().strip()







def main():
    uname = input("Username here: ")

    password = findpword(uname)

    if password != None:
        if passwordcheck(password,3):
            print("Access granted")
    else:
        print("Check username")
main()
