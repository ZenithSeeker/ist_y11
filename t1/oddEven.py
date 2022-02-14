#Samuel Pitchforth
#9/2/22
#odd or even

def oddEven():
    #gets a number as input
    num = int(input("Enter a number, \nthe program will determine if it is "
                    "even or odd: "))


    if((num%2) == 0):
        print("the number " + str(num) + " is even!")
    else:
        print("the number " + str(num) + " is odd!")
        
