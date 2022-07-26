# ------------------------------------------------------------------------------#
#  Tic Tac Toe Program
# ------------------------------------------------------------------------------#
#  Purpose:
#  Author: Samuel Pitchforth
#  Date: 20/07/2020
# ------------------------------------------------------------------------------#
import time
import random


# ------------------------------------------------------------------------------#
#  main()
# ------------------------------------------------------------------------------#
#  Purpose: Highest level of program, calls subroutines in the correct order.
#  Running this
# ------------------------------------------------------------------------------#
def main():
    # when this flag is true, the user wants to leave, and the program loop will
    # be bypassed
    exit_flag = False
    # if password_check successfully verifies the user, the rest of the program
    # run
    if passwordCheck("1234", 4):
        # menu returns True when the player wishes to exit, and thus the loop
        # will brewk
        while not menu():
            pass
        print("Thank you for playing")
    else:
        print("There have been 4 incorrect attempts."
              " The program will exit now")


# ------------------------------------------------------------------------------#
#  getboardsize()
# ------------------------------------------------------------------------------#
#  Purpose:Returns the user's desired board size as an int. This must be within
#  the range 3-30 inclusive.
# ------------------------------------------------------------------------------#
def getboardsize():
    list_of_valid_sizes = [""] * 50
    for i in range(3, 31):
        list_of_valid_sizes[i] = str(i)
    size = int(get_input_in_list(list_of_valid_sizes,
                                 'Enter a board size in the range 3-30'))

    return size


# ------------------------------------------------------------------------------#
#  menu()
# ------------------------------------------------------------------------------#
#  Purpose: The menu page for the program. Displays options to the user and
#  calls various subroutines depending on the user's choices. Returns an exit
#  flag which becomes true when the user wants to exit
# ------------------------------------------------------------------------------#
def menu():
    exit_flag = False
    print("Welcome TO TIC-TAC-TOE")
    print("imagine a delightful welcome screen right here")
    print("You got 3 options\n"
          "1. Player Vs Computer\n"
          "2. Instructions\n"
          "3. Exit")
    answer = int(get_input_in_list(["1", "2", "3", "4", "5"], "Enter your choice here:"))
    if answer == 1:
        display_text_file("instructions.txt")

    elif answer == 2:
        size = getboardsize()
        player_computer_game(size)
    elif answer == 3:
        size = getboardsize()
        player_player_game(size)
    elif answer == 4:
        getboardsize()
        computer_computer_game(size)

    else:
        exit_flag = True
    return exit_flag


# ------------------------------------------------------------------------------#
#  print_grid(board, size)
# ------------------------------------------------------------------------------#
#  Purpose: Displays the board to the user
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


# ------------------------------------------------------------------------------#
#  circle_or_cross(value)
# ------------------------------------------------------------------------------#
#  Purpose: Returns a string of the symbol represented by the integer within
#  the program. Passing it a -1 or 1 will return a "O" and a "X" respectively
#  while any other value will result in a "-". This is used by the print_grid()
#  function to get the conventional symbols used in the game.
# ------------------------------------------------------------------------------#
def circle_or_cross(value):
    if value == -1:
        symbol = "O"
    elif value == 1:
        symbol = "X"
    else:
        symbol = "-"
    return symbol


# ------------------------------------------------------------------------------#
#   password_check(password, numofguesses)
#   Verifies the user by giving them a number of attempts to input the correct
#   password. The password must be a string, and numofguesses
# ------------------------------------------------------------------------------#
def password_check(password, numofguesses):
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
    else:
        print("draw")


def computer_move(board, size):
    move = random.randint(0, size * size - 1)
    while board[move] != 0:
        move = random.randint(0, size * size - 1)

    return move


def get_user_move(name, board, size):
    valid_moves = [""] * size * size
    for i in range(len(valid_moves)):
        valid_moves[i] = str(i + 1)

    print("It is your turn " + name)

    move = int(get_input_in_list(valid_moves, "Move please: ")) - 1
    while board[move] != 0:
        print("sorry this square is already taken")
        move = int(get_input_in_list(valid_moves, "Move please: ")) - 1
    return move


# ------------------------------------------------------------------------------#
#  check_win(board, size)
# ------------------------------------------------------------------------------#
#  Purpose: Returns a integer based on the status of the game passed to the
#  subroutine. Moves must be represented by a 1 or -1 for the respective
#  players. Returns a 1 or -1 for a win by the player controlling that counter
#  , a 0 for an incomplete game, and 999 for a full board with no winning moves
#  signifying a draw.
# ------------------------------------------------------------------------------#

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

    for i in range(size * size):
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
