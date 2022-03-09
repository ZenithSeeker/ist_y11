size = abs(int(input("size: ")))

##formatting with the spaces to make it look pretty
spaces = size * 2 - 1
spaces = 1 + int(len(str(spaces)))

for i in range(1, size + 1):
    for j in range(size):
        print(j + i, end=(" " * (spaces - int(len(str(j + i))))))

    print("")
