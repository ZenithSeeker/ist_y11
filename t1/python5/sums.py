def divider():
    #makes a nice line
    print("--------------")

def sums():
    odd_sum = 0
    even_sum = 0
    num_count = int(input("How many numbers: "))
    for i in range(num_count):
        temp_num = int(input("Enter number {}:".format(i + 1)))
        if (temp_num % 2) == 0:
            even_sum += temp_num
        else:
            odd_sum += temp_num

    divider()
    print("Even:    " + str(even_sum))
    print("Odd:     " + str(odd_sum))
    divider()
    print("Total:   " + str(odd_sum + even_sum))
    divider()
sums()