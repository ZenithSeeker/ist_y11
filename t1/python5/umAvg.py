#adds and averages a list of inputs
def sumAvg():
    total = 0
    for i in range(0,5):
        #get number
        new_num = float(input("Num " + str(i + 1) + ": "))
        #add to running total
        total += new_num

    #output calculations
    print(total)

    print(total/5)