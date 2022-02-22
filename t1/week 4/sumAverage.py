def sumAverage():
    score1 = float(input("Score1: "))
    score2 = float(input("Score2: "))
    score3 = float(input("Score3: "))
    score4 = float(input("Score4: "))
    score5 = float(input("Score5: "))

    print("FLoating point calcs:")
    sum = score1 + score2 + score3 + score4 + score5
    print("Sum: " + str(sum))
    print("Avg: " + str(sum/5))
    print("-------")

    print("Integer display:")
    isum = int(sum)
    print("Sum: " + str(isum))
    print("Avg: " + str(int(isum / 5)))

    print("-------")

    print("Rounding display:")


    print("Sum: " + str(round(sum)))
    print("Avg: " + str(round(sum / 5)))

