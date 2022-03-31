def validate_num():
    num = int(input("Enter a number between 1-7: "))
    while num < 1 or num > 7:
        print("Invalid input error, check your answer is between 1 and 7")
        num = int(input("Enter a number between 1-7: "))

    return num



def validate_length():
    sentence = input("Enter some words: ")
    while len(sentence) < 12:
        print("error. TOo short")
        sentence = input("Try again: ")
    return sentence

def repeat(string, num):


    for i in range(num):
        print(string)


def all_together():
    run = True
    while run:
        repeated_string = validate_length()
        num = validate_num()
        repeat(repeated_string, num)
        run = input("Repeat? (y/n)")
        if run == "n":
            run = False
    print("cya")


all_together()