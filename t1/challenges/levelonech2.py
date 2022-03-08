num1 = int(input("Num1:"))
num2 = int(input("Num2:"))
if num1 % 2 == 1:
    total = num2
while num1 != 1:
    num1 = int(num1/2)

    num2 = num2 * 2
    if num1 % 2 == 1:
        total += num2




print(total)

