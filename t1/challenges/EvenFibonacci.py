small = 0
lead = 1
hold = 0

total = 0
while 4000000 > lead:
    hold = lead
    lead = lead + small
    small = hold
    print(lead)
    if lead % 2 == 0 and lead < 4000000:
        total += lead
print("Total: " + str(total))

