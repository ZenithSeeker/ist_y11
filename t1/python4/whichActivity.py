def whichActivity():
    temp = int(input("Enter the temp: "))
    if temp >= 30:
        print("swim")
    elif temp >=20:
        print("golf")
    else:
        print("heater")
whichActivity()