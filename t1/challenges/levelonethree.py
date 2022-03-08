
file = open("inputtext.txt", "r")

uprun = True
for line in file:
    runcount = 1
    line = line.strip()
    data = line.split()

    if len(data) > 1:


        if line[1] > line[0]:
            uprun = True
        else:
            uprun = False
        for i in range(len(data)):
            if line[i + 1] > line[1] and uprun == False:
                uprun = True
                runcount += 1
            elif not line[i + 1] > line[1] and uprun == True:
                uprun = False
                runcount += 1
            print(runcount)





    print(data)