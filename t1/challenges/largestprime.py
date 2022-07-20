# NUMBER
import math
number = 600851475143
tnum = number
tree = []

def check_prime(num):
    prime = True
    for i in range(2, num):
        if num%i == 0:
            prime = False
    return prime





for i in range(2,number):
    if check_prime(i):
        while tnum % i == 0:
            tree.append(i)
            tnum = int(tnum/i)
    if math.prod(tree) == number:
        break
print(tree)
