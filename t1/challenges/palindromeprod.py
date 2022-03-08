
high = 0
for i in range(999, 99, -1):
    for s in range(999, 99, -1):
        num = i * s

        if str(i * s)[::-1] == str(i * s) and num > high:
            high = num
            one = i
            two = s

print(i, s, high)



