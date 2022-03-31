# NUMBER
number = 60085147514

def prime(num):
    notprim = False

    for i in range(2, int(num / 2 + 1)):

        if num % i == 0:
            notprim == True
            return notprim
    return notprim


def largenum(number):
    for i in range(int(number / 2), 1, -1):
        if number % i == 0
            prime(i):
            print(i)
            break
