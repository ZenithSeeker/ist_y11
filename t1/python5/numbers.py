size = int(input("size: "))

for i in range(1, size + 1):
    for j in range(size):
        print(j + i, end="  ")
    print("")
