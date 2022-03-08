#Orders inputs
def ascending():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    num3 = int(input("Enter num3: "))
    if num1 >= num2 and num1 >= num3:
        print(num1, end=(" "))
        if num2 >= num3:
            print(num2, num3)
        else:
            print(num3, num2)
    elif num2 >= num1 and num2 >= num3:
        print(num2, end=(" "))
        if num1 >= num3:
            print(num1, num3)
        else:
            print(num1, num3)
    elif num3 >= num1 and num3 >= num3:
        print(num3, end=(" "))
        if num2 >= num1:
            print(num2, num1)
        else:
            print(num1, num2)



ascending()