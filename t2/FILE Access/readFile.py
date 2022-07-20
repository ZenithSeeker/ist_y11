def readFile():
    f = open("read.txt", "r")
    [print(line.strip()) for line in f.readlines()]
    f.close

readFile()

