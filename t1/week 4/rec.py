

def rectangle():
    length = float(input("Length: "))
    width = float(input("Width: "))

    perim = 2*length + 2 * width
    area = length * width
    print(str(area) + ","+ str(perim))

rectangle()