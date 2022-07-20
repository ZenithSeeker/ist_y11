from pass1 import passwordcheck

def findpword(uname):
    with open("passworddat.txt", "r") as f:
        for line in f:
            if line.strip() == uname:
                return f.readline().strip()






def main():
    uname = input("Username here: ")

    if passwordcheck(findpword(uname),3):
        print("Access granted")
main()
