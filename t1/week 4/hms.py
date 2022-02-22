#seconds --> hour minute seconds

def hms():
    time = int(input("Enter the time in seconds: "))
    hour = int(time/3600)
    time = time % 3600
    minute = int(time/60)
    seconds = time % 60
    print("This is: " + str(hour) + ":" + str(minute)+ ":" + str(seconds))

hms()
