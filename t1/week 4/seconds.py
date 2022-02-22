# gives input in hours minutes seconds and get returned the number of seconds left

def seconds():
    hour = int(input("Enter the number of hours: "))
    minute = int(input("Enter the number of minutes: "))
    second = int(input("Enter the number of seconds: "))

    time = second + (60 * minute) + 3600 * hour
    print("Total seconds: " + str(time))

seconds()
