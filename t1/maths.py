#Samuel Pitchforth
#9/2/22
#tests operators on ints and floats

def maths():
    print(5 + 7 * 2) # multiplies then adds
    print(5 * 7 + 2)# multiplies then adds
    print(3 * 12 /5)# multiplies then divides
    print(3 * (12/5))#divides then multiplies
    print(3 * 12. /5) # multiplies then divides (36. /5 gives )
    print(3 * (12. / 5))#divides then multiplies
    print(3 * 5. * 2/ (7%2))# multiplies then divides by 1


def integers():
    n = int(input("Enter n: ")) ## input for n (type: int)

    m = int(input("Enter m: ")) ## input for m (type: int)
    

    print("n + m is " + str(n + m)) ## add m and n
    print("n - m is " + str(n - m)) ## subtract m from n
    print("n * m is " + str(n * m)) ## multiply m and n
