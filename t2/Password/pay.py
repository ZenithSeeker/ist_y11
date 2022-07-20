#loads the data into a structure called data
def loaddata(file):
    f = open(file, "r")
    data = f.readlines()
    f.close()
    return data


#
def process(data):
    data = data.split(",")
    pay = (float(data[2]) * float(data[3])) + (float(data[2]) * float(data[4]) * 1.5)
    name = (data[0] + data[1])
    return name, str(round(pay, 2))


def writeout(data):
    name, pay = data
    with open("payamounts.txt", "a") as f:
        f.write(name + " $" +  pay + "\n")

def main():

    for i in loaddata("workclock.txt"):
        writeout(process(i))


main()