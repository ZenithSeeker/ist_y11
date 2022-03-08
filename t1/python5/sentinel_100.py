def sentinel_100():
    total = 0
    question = 0
    while total < 100:
        total += int(input("Please enter a number: "))
        question += 1
        print("Numbers: " + str(question) + " sum = " + str(total))
    print("Sentnel 100???")


sentinel_100()
