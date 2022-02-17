def avgTemp():
    total = 0
    data = str(input("Enter the temparature for each day seperated by a comma and a space: "))
    data = data.split(", ")
    for i in data:

        total += float(i)
    print(total/len(data))

avgTemp()