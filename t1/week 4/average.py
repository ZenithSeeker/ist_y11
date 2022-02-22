#Samuel Pitchforth
#22/2
#Average

def average():
    score1 = float(input("Score1: "))
    score2 = float(input("Score2: "))
    score3 = float(input("Score3: "))
    score4 = float(input("Score4: "))
    score5 = float(input("Score5: "))

    avg = (score1 + score2 + score3 + score4 + score5)/5

    print("your average is " + str(avg))