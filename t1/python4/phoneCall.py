def phonecall():
    time = int(input("Time on phone in minutes: "))
    price = 1.99
    if time >= 3:
        price += 2
        time -= 3
        price += (0.45 * time)
    else:
        price += 2

    price = round(price, 2)
    print(price)
phonecall()