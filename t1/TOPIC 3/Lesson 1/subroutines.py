from larger import main as lmain
from swap import main as smain
from convert import main as cmain



def main():
    print("Subroutines!!!")
    print("----------------")
    print("Make a choice")
    print("a. FIND LARGEST")
    print("b. SwAP VALUES")
    print("Faremjeiet to celsius")
    choice = input("CHOICE: ")
    print("----------------------------------")
    if choice == 'a':
        print("LARGER")
        print("-------------------------")
        lmain()
        print("-------------------------")
    elif choice == 'b':
        print("SWAP")
        print("-------------------------")
        smain()
        print("-------------------------")
    elif choice == "c":
        print("CONVert")
        print("-------------------------")
        cmain()
        print("-------------------------")
    else:
        print("-------------------------")
        lmain()
        print("-------------------------")
        smain()
        print("-------------------------")
        cmain()
        print("-------------------------")


main()