def sentinalList():
    with open("names.txt", "r") as f:
        line = f.readline()
        while line != "999":
            print(line.strip())
            line = f.readline()
sentinalList()