def writeFile():
    f = open("write.txt", "w")
    f.write("HELLO\n")
    f.write("normal rules apply?")
    f.close()
writeFile()