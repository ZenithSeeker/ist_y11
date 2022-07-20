for i in range(1, 101):
    three = i% 3
    five = i % 5
    if three == 0 and five != 0:
        print("FIZZ")
    if i % 5 == 0 and three != 0:
        print("BUZZ")
    if three == 0 and five == 0:
        print("FIZZBUZZ")
    else:
        print(i)



def swap(item1, item2):
    return item1, item2

