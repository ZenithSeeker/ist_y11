def stars():
    num = int(input("how many stars in the night sky?"))
    for i in range(1, num + 1):
        print("* " * i)
stars()