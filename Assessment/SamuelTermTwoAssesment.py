# ------------------------------------------------------------------------------#
#  Tic Tac Toe Program
# ------------------------------------------------------------------------------#
#  Purpose: Password protected game of tic-tac-toe
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
    if password_check("1234", 4):
        # menu returns True when the player wishes to exit, and thus the loop
        # will break
        while not exit_flag:
            exit_flag = menu()

        # This runs once the menu loop is ended, and the program is closing
        print("------------------------------------------")
        print("Thank you for playing")
    # If the password was not guessed, communicate this to the user
    # before ending the program
    else:
        print("------------------------------------------")
        print("There have been 4 incorrect attempts.\n"
              "The program will exit now")
        time.sleep(2)


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
                                 'Enter a board size in the range 3-30: '))

    return size


# ------------------------------------------------------------------------------#
#  menu()
# ------------------------------------------------------------------------------#
#  Purpose: The menu page for the program. Displays options to the user and
#  calls various subroutines depending on the user's choices. Returns an exit
#  flag which becomes true when the user selects the exit option
# ------------------------------------------------------------------------------#
def menu():
    exit_flag = False
    print("------------------------------------------\n\n\n")
    print(" _       __     __                             __\n"
          "| |     / /__  / /________  ____ ___  ___     / /_____       \n"
          "| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \ \n"
          "| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /      \n"
          "|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/___\__/\____/       \n"
          " /_  __(_)____   /_  __/___ ______   /_  __/___  ___\n"
          "  / / / / ___/    / / / __ `/ ___/    / / / __ \/ _ \ \n"
          " / / / / /__     / / / /_/ / /__     / / / /_/ /  __/\n"
          "/_/ /_/\___/    /_/  \__,_/\___/    /_/  \____/\___/\n\n\n")
    print("------------------------------------------")
    print("Please select one of the following\n"
          "1. Instructions\n"
          "2. Player Vs Comp\n"
          "3. Player Vs Player\n"
          "4. Comp Vs Comp\n"
          "5. Exit"
          )

    answer = int(get_input_in_list(["1", "2", "3", "4", "5"], "Enter your choice here: "))
    if answer == 1:
        print("------------------------------------------")
        display_text_file("instructions.txt")

    elif answer == 2:
        size = getboardsize()
        tic_tac_toe_game(size, player1_is_comp=False, player2_is_comp=True)
    elif answer == 3:
        size = getboardsize()
        tic_tac_toe_game(size, player1_is_comp=False, player2_is_comp=False)
    elif answer == 4:
        size = getboardsize()
        tic_tac_toe_game(size, player1_is_comp=True, player2_is_comp=True)
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
    attempts = "attempts"
    verify = False
    print("------------------------------------------")
    guess = input("Enter password here: ")
    while not verify and numofguesses > 0:
        if guess == password:
            verify = True
        else:
            numofguesses -= 1
            if numofguesses > 0:
                print("------------------------------------------")
                print("Incorrect Password")
                if numofguesses == 1:
                    attempts = "attempt"

                print("You have " + str(numofguesses)
                      + " " + attempts + " remaining")
                print("------------------------------------------")
                guess = input("Retry here: ")
    return verify


def tic_tac_toe_game(size, player1_is_comp, player2_is_comp):
    board = [0] * size * size
    game_over = False
    if not player1_is_comp:
        print("------------------------------------------")
        namep1 = input("Player 1 please enter your name here: ")
    if not player2_is_comp:
        print("------------------------------------------")
        namep2 = input("Player 2 please enter your name here: ")
    print("------------------------------------------")

    solo_computer = player1_is_comp ^ player2_is_comp

    while not game_over:
        print_grid(board, size)
        if player1_is_comp:
            computer_turn(1, board, size, solo_computer)
        else:
            board[get_user_move(namep1, board, size)] = 1

        if check_win(board, size) != 0:
            game_over = True
        else:
            print_grid(board, size)
            if player2_is_comp:
                computer_turn(2, board, size, solo_computer)
            else:
                board[get_user_move(namep2, board, size)] = -1
        if check_win(board, size) != 0:
            game_over = True
            print_grid(board, size)

    winner = check_win(board, size)
    if winner == 1:
        if player1_is_comp:
            print("Computer 1 wins")
        else:
            print(namep1 + " wins!")
    elif winner == -1:
        if player2_is_comp:
            print("Computer 2 wins")
        else:
            print(namep2 + " wins!")
    else:
        print("This game ended in a draw")




def computer_turn(comp_num, board, size, solo_computer):
    print("------------------------------------------")
    if not solo_computer:
        print("It is Computer " + str(comp_num) + "'s turn")
    else:
        print("It is the computer's turn")
    print("------------------------------------------")
    print(".", end="")
    time.sleep(0.4)
    print(".", end="")
    time.sleep(0.4)
    print(".")
    time.sleep(0.4)
    if comp_num == 2:
        counter = -1
    else:
        counter = 1
    board[computer_move(board, size)] = counter


def computer_move(board, size):
    move = random.randint(0, size * size - 1)
    while board[move] != 0:
        move = random.randint(0, size * size - 1)
    return move


def get_user_move(name, board, size):
    valid_moves = [""] * size * size
    for i in range(len(valid_moves)):
        valid_moves[i] = str(i + 1)
    print("------------------------------------------")
    print("It is your turn " + name)
    move = int(get_input_in_list(valid_moves, "Enter move here: ")) - 1
    while board[move] != 0:
        print("This square already has a counter in it. Please try again")
        move = int(get_input_in_list(valid_moves, "Enter move here: ")) - 1
    return move


# ------------------------------------------------------------------------------#
#  check_win(board, size)
# ------------------------------------------------------------------------------#
# Parameter types:
# Name: board, Type: List, Array
# Name: size, Type: Integer
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


# ------------------------------------------------------------------------------#
#  display_text_file(file_path):
# ------------------------------------------------------------------------------#
# Parameter types:
# Name: file_path, Type: String
# ------------------------------------------------------------------------------#
#  Purpose: Opens the text file at the specified location and displays it to
#  the user sequentially.
# ------------------------------------------------------------------------------#
def display_text_file(file_path):
    f = open(file_path, "r")
    for line in f:
        # is this allowed?
        print(line.strip())
    f.close()


# ------------------------------------------------------------------------------#
#  in_list(value, list_to_check)
# ------------------------------------------------------------------------------#
# Parameter types:
# Name: value, Type: Any
# Name: list_to_check, Type: List, Array
# ------------------------------------------------------------------------------#
#  Purpose: Checks if a given value is contained within a given list. Returns
#  True if it is, and False if it is not.
# ------------------------------------------------------------------------------#
def in_list(value, list_to_check):
    in_list = False
    for i in range(len(list_to_check)):
        if value == list_to_check[i]:
            in_list = True
    return in_list

# ------------------------------------------------------------------------------#
#  get_input_in_list(valid_inputs_list, user_prompt)
# ------------------------------------------------------------------------------#
# Parameter types:
# Name: valid_inputs_list, Type: List, Array
# Name: user_prompt, Type: String
# ------------------------------------------------------------------------------#
#  Takes in a list of valid values and a user prompt. Uses the prompt to get an
#  user input and if the input is not contained within the list of valid inputs
#  a new user input is gained. This repeats until a valid input has been gained
# ------------------------------------------------------------------------------#
def get_input_in_list(valid_inputs_list, user_prompt):
    print("------------------------------------------")
    value = input(user_prompt)

    while not in_list(value, valid_inputs_list):
        print("------------------------------------------")
        print("That is not a valid input. Please try again.")
        value = input(user_prompt)
    return value



main()
