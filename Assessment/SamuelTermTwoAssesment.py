# ------------------------------------------------------------------------------#
#  Tic Tac Toe Program
# ------------------------------------------------------------------------------#
#  Purpose:
#  Author: Samuel Pitchforth
#  Date: 1/07/2020
# ------------------------------------------------------------------------------#
import time
import random


# ------------------------------------------------------------------------------#
#  main()
# ------------------------------------------------------------------------------#
#  Purpose: Highest level of program, calls subroutines and allows the code to
# be run
# ------------------------------------------------------------------------------#
def main():
    # when this flag is true, the user wants to leave, and the program loop will
    # be bypassed
    exit_flag = False
    # if password_check successfully verifies the user, the rest of the program
    # run
    if passwordCheck("1234", 4):
        while not menu():
            pass
        print("Thank you for playing")
    else:
        print("There have been 4 incorrect attempts. The program will now exit")


def menu():
    exit_flag = False
    print("Welcome TO TIC-TAC-TOE")
    print("imagine a delightful welcome screen right here")
    print("You got 3 options\n"
          "1. Player Vs Computer\n"
          "2. Instructions\n"
          "3. Exit")
    answer = get_input_in_list(1, 3, "Enter your choice here:")
    if answer == 1:
        player_computer_game(get_input_in_list(2, 50, 'enter a board size betwen 2-50'))
    elif answer == 2:
        display_text_file("instructions.txt")
    else:
        exit_flag = True
    return exit_flag


# ------------------------------------------------------------------------------#
#   printGrid()
#   prints current status of the grid
# ------------------------------------------------------------------------------#



def print_grid(board, size):
    print("", end="   ")
    print()
    for y in range(size):
        print("-" * (size * 4 + 2))
        print(" | ", end="")
        for x in range(size):
            print(circle_or_cross(board[y * size + x]), end=" | ")
        print()
    print("-" * size * 4)


def circle_or_cross(value):
    if value == -1:
        symbol = "O"
    elif value == 1:
        symbol = "X"
    else:
        symbol = "-"
    return symbol


# ------------------------------------------------------------------------------#
#   password_check(password, numofguesses, failuremsg)
#   Verifies the user by giving them a number of attempts to input the correct
#   password. 4 Incorrect guesses will cause the program to exit
# ------------------------------------------------------------------------------#
def passwordCheck(password, numofguesses):
    verify = False
    guess = input("Enter password here: ")
    while not verify and numofguesses > 0:
        if guess == password:
            verify = True
        else:
            numofguesses -= 1
            if numofguesses > 0:
                print("Incorrect Password")
                print(f"{numofguesses} tries left")
                guess = input("Retry here: ")
    return verify


def player_computer_game(size):
    board = [0] * size * size
    game_won = False
    name = input("Please enter your name here: ")

    print("-" * 70)

    while not game_won:
        print_grid(board, size)
        board[get_user_move(name, board, size)] = 1

        print_grid(board, size)
        if check_win(board, size) != 0:
            game_won = True
        else:
            print(".", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            board[computer_move(board, size)] = -1
    winner = check_win(board, size)
    if winner == 1:
        print("THE WINNER IS " + winner)
    else:print("draw")


def computer_move(board, size):
    move = random.randint(0, size * size - 1)
    while board[move] != 0:
        move = random.randint(0, size * size - 1)

    return move


def get_user_move(name, board, size):
    valid_entries = [""]
    for i in range(size*size):

    print("It is your turn " + name)
    move = int(get_input_in_list(1, size * size + 1, "Move please: ")) - 1
    while board[move] != 0:
        print("sorry this square is already taken")
        move = int(get_input_in_list(1, size * size + 1, "Move please: ")) - 1
    return move


def check_win(board, size):
    board_full = True
    game_status = 0
    # check diagonal cases
    diagonal_total = 0
    other_diagonal_total = 0
    for i in range(size):
        diagonal_total += board[(size + 1) * i]
        other_diagonal_total += board[(i + 1) * (size - 1)]
    if diagonal_total == size or diagonal_total == size * -1:
        game_status = int(diagonal_total / size)
    if other_diagonal_total == size or other_diagonal_total == size * -1:
        game_status = int(other_diagonal_total / size)

    # check rows
    for square in range(len(board)):
        if square % size == 0:
            row_total = 0
        row_total += board[square]
        if row_total == size or row_total == size * -1:
            game_status = int(row_total / size)

    # check columns
    column_counter = [0] * size
    for square in range(len(board)):
        column_counter[square % size] += board[square]
    for cell in range(len(column_counter)):
        if column_counter[cell] == size or column_counter[cell] == size * -1:
            game_status = int(column_counter[cell] / size)

    for i in range(size*size):
        if board[i] == 0:
            board_full = False
    if game_status == 0 and board_full:
        game_status = 999
    return game_status


def display_text_file(file_path):
    f = open(file_path, "r")
    for line in f:
        # is this allowed?
        print(line.strip())
    f.close()


def in_list(value, list_to_check):
    in_list = False
    for i in range(len(list_to_check)):
        if value == list_to_check[i]:
            in_list = True
    return in_list


# ------------------------------------------------------------------------------#
#   error_free_input(valid_values, user_prompt)
#   Takes in a list of valid values and a user prompt as a string
#   Gets an input from the user that is in the valid values list
#
# ------------------------------------------------------------------------------#
def get_input_in_list(valid_inputs_list, user_prompt):
    value = input(user_prompt)
    while not in_list(value, valid_inputs_list):
        value = input(user_prompt)
    return value


def total():
    pass


main()
