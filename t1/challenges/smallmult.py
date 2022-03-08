import numpy as np

nosolve = True
inc = 21
while nosolve:
    count = 0
    for i in range(11, 21):
        if inc % i == 0:
            count += 1
    print(inc)
    if count == 10:
        print("solved")
        print(inc)
        nosolve = False




    inc += 1