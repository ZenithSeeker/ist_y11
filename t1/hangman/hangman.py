# Jotaro, Oil, Samira
# 31/03/2022
# Hagman

import turtle
import random
import math


def hangman():
    easyword = ["doll"]
    midword = ["castle"]
    hardword = ["gobbledegook", "syzygy"]
    print("Welcome to the Hangman program")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    guessed = []
    dif = input("Which difficulty? e.g. 1 : ")

    while dif != "1" and dif != "2" and dif != "3":
        print("not valid sorry")
        dif = input("Which difficulty? e.g. 1 : ")

    if dif == "1":
        wordlist = easyword
    elif dif == "2":
        wordlist = midword
    else:
        wordlist = hardword

    word = random.choice(wordlist)

    playerpov = ["_"] * len(word)
    print("BEGIN GAME!")

    attempts = 10
    won = False
    while attempts > 0 and not won:
        guess = False
        print(''.join(playerpov))
        print("you have " + str(attempts) + " left ")
        print("Guessed: ", guessed)

        cletter = input("Guess here: ")
        while len(cletter) != 1 or cletter in guessed:
            print("Bad ")
            cletter = input("Guess here: ")

        guessed.append(cletter)

        for i in range(len(word)):
            if cletter == word[i]:
                playerpov[i] = cletter
                guess = True

        if not guess:
            attempts -= 1

        if ''.join(playerpov) == word:
            print(''.join(playerpov))
            print("you are good at this")
            won = True



    if not won:
        print("GGEZ uninstall")

hangman()

