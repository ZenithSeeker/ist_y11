def n_ints():
    total = 0
    num_of_nums = int(input("How many numbers to enter: "))
    print("Enter {} numbers".format(num_of_nums))
    for i in range(num_of_nums):
        total += int(input("Enter num " + str(i +1) + ": "))
    print(total)