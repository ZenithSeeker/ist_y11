# ------------------------------------------------------------------------------#
#  Tic Tac Toe Program
# ------------------------------------------------------------------------------#
#  Purpose: Password protected game of tic-tac-toe
#  Author: Samuel Pitchforth
#  Date: 12/08/2022
# ------------------------------------------------------------------------------#
import time
import random


# Used often for formatting purposes. Making this global makes future
# changes to formatting far easier as only one thing must be changed
break_line = "--------------------------------------------------------" \
                 "---------------"

# ------------------------------------------------------------------------------#
#  main()
# ------------------------------------------------------------------------------#
#  Purpose: Highest level of program, calls subroutines in the correct order
# ------------------------------------------------------------------------------#
def main():
    exit_flag = False
    # if password_check successfully verifies the user, the rest of the program
    # run
    if password_check("1234", 4):
        # menu returns True when the player wishes to exit, and thus the loop
        # will break
        while not exit_flag:
            exit_flag = menu()

        print(break_line)
        print("Thank you for playing")
    # If the password was not guessed, communicate this to the user
    # before ending the program
    else:
        print(break_line)
        print("There have been 4 incorrect attempts.\n"
              "The program will exit now")
    # Gives time for user to read the exit messages
    time.sleep(2)


# ------------------------------------------------------------------------------#
#  menu()
# ------------------------------------------------------------------------------#
#  Purpose: The menu page for the program. Displays options to the user and
#  calls various subroutines depending on the user's choices. Returns an exit
#  flag which becomes true when the user selects the exit option
# ------------------------------------------------------------------------------#
def menu():
    exit_flag = False
    # Display welcome graphic
    print(break_line + "\n\n\n")
    print("      _       __     __                             __\n"
          "     | |     / /__  / /________  ____ ___  ___     / /_____       \n"
          "     | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \ \n"
          "     | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /      \n"
          "     |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/___\__/\____/       \n"
          "    /_  __(_)____   /_  __/___ ______   /_  __/___  ___\n"
          "     / / / / ___/    / / / __ `/ ___/    / / / __ \/ _ \ \n"
          "    / / / / /__     / / / /_/ / /__     / / / /_/ /  __/\n"
          "   /_/ /_/\___/    /_/  \__,_/\___/    /_/  \____/\___/\n\n\n")
    print(break_line)
    print("Please choose one of the following:\n"
          "    1. Instructions\n"
          "    2. Player Vs Comp\n"
          "    3. Player Vs Player\n"
          "    4. Comp Vs Comp\n"
          "    5. Exit"
          )

    answer = get_int_input_in_range("Enter your choice here: ", 1, 5)
    if answer == 1:
        print(break_line)
        display_text_file("instructions.txt")
    elif answer == 5:
        exit_flag = True
    else:
        # If user starts a game get the size
        size = get_int_input_in_range("Enter a board size in the range 3-30: "
                                      , 3, 30)
        # set the players to computers or human players according to the chosen
        # gamemode
        if answer == 2:
            player1_is_comp = False
            player2_is_comp = True
        elif answer == 3:
            player1_is_comp = False
            player2_is_comp = False
        else:
            player1_is_comp = True
            player2_is_comp = True
        # Call the tic_tac_toe_game with the variables
        tic_tac_toe_game(size, player1_is_comp, player2_is_comp)
    return exit_flag


# ------------------------------------------------------------------------------#
#  print_grid(board, size)
# ------------------------------------------------------------------------------#
#  Purpose: Displays the board to the user
# ------------------------------------------------------------------------------#
def print_grid(board, size):
    space = "                 "
    print()
    # loop over each row
    for y in range(size):
        # print a horizontal bar
        print(space + "-" * (size * 4 + 2))
        # print a single vertical
        print(space + " | ", end="")
        # All in the same line, add the symbol and then another vertical bar
        for x in range(size):
            print(circle_or_cross(board[y * size + x]), end=" | ")
        # End the previous line
        print()
    # print a horizontal bar
    print(space + "-" * (size * 4 + 2))


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
#   password_check(password, num_of_guesses)
# ------------------------------------------------------------------------------#
#  Purpose: Verifies the user by giving them a number of attempts to input the
#  correct password.
# ------------------------------------------------------------------------------#
def password_check(password, num_of_guesses):
    is_plural = True
    verify = False
    password = str(password)

    print(break_line)
    guess = input("Enter password here: ")

    while not verify and num_of_guesses > 0:
        if guess == password:
            verify = True
        else:
            num_of_guesses -= 1
            if num_of_guesses > 0:
                print(break_line)
                print("Incorrect Password")
                if num_of_guesses == 1:
                    is_plural = False
                print("You have " + str(num_of_guesses)
                      + " attempt" + "s" * is_plural + " remaining")
                print(break_line)
                guess = input("Retry here: ")
    return verify


# ------------------------------------------------------------------------------#
#  tic_tac_toe_game(size, player1_is_comp, player2_is_comp)
# ------------------------------------------------------------------------------#
#  Purpose: Runs the main game loop and calls the relevant submodules
# ------------------------------------------------------------------------------#
def tic_tac_toe_game(size, player1_is_comp, player2_is_comp):
    board = [0] * size * size
    game_over = False
    # If it is a person, get their name
    if not player1_is_comp:
        print(break_line)
        namep1 = input("Player 1 please enter your name here: ")
    # If it is a person, get their name
    if not player2_is_comp:
        print(break_line)
        namep2 = input("Player 2 please enter your name here: ")
    print(break_line)

    # XOR operator. solo_computer is only true if exactly one player is
    # a computer
    solo_computer = player1_is_comp ^ player2_is_comp

    while not game_over:
        print_grid(board, size)
        # Player 1's turn
        if player1_is_comp:
            computer_turn(1, board, size, solo_computer)
        else:
            board[get_user_move(namep1, board, size)] = 1

        if check_win(board, size) != 0:
            game_over = True
        # This stops player 2 having a go if the game ends here
        else:
            # Player 2's turn
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
            if solo_computer:
                print("The computer wins!")
            else:
                print("Computer 1 wins!")
        else:
            print(namep1 + " wins!")
    elif winner == -1:
        if player2_is_comp:
            if solo_computer:
                print("The computer wins!")
            else:
                print("Computer 2 wins!")
        else:
            print(namep2 + " wins!")
    else:
        print("This game ended in a draw")


# ------------------------------------------------------------------------------#
#  computer_turn(comp_num, board, size, solo_computer)
# ------------------------------------------------------------------------------#
# Parameters:
# comp_num: Int equal to 1 or 2. Changes certain messages to reflect which
#           computer is under control, and which counter it places
# board: the board to place the counters on
# size: the board size as an integer
# solo_computer: Boolean that changes messages slightly in the case of exactly
#               one computer controlled player
# ------------------------------------------------------------------------------#
#  Purpose: Creates various visual elements relating to the computers turn
#  and executes the computers move.
# ------------------------------------------------------------------------------#
def computer_turn(comp_num, board, size, solo_computer):
    print(break_line)
    if not solo_computer:
        print("It is Computer " + str(comp_num) + "'s turn")
    else:
        print("It is the computer's turn")
    print(break_line)
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


# ------------------------------------------------------------------------------#
#  computer_move(board, size)
# ------------------------------------------------------------------------------#
#  Purpose: Generate computer move
# ------------------------------------------------------------------------------#
def computer_move(board, size):
    move = random.randint(0, size * size - 1)
    while board[move] != 0:
        move = random.randint(0, size * size - 1)
    return move


# ------------------------------------------------------------------------------#
#  get_user_move(name, board, size)
# ------------------------------------------------------------------------------#
#  Purpose: Get the users move
# ------------------------------------------------------------------------------#
def get_user_move(name, board, size):
    print(break_line)
    print("It is your turn " + name)
    move = get_int_input_in_range("Enter move here: ", 1, size * size) - 1
    while board[move] != 0:
        print("This square already has a counter in it. Please try again")
        move = get_int_input_in_range("Enter move here: ", 1, size * size) - 1
    return move


# ------------------------------------------------------------------------------#
#  check_win(board, size)
# ------------------------------------------------------------------------------#
# Parameters:
# board: The board to check. Is a 1d array
# size: the board dimension as an integer
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
        # Adds up each diagonal
        # The diagonals increment at n+1 and n-1 respectively.
        diagonal_total += board[(size + 1) * i]
        other_diagonal_total += board[(i + 1) * (size - 1)]

    # Equal absolute value size means that diagonal is one type of counter only
    if diagonal_total == size or diagonal_total == -size:
        # Find which counter it is
        game_status = int(diagonal_total / size)

    if other_diagonal_total == size or other_diagonal_total == -size:
        game_status = int(other_diagonal_total / size)

    # check each row
    for y in range(size):
        row_total = 0
        for x in range(size):
            # for each value in row, add to total
            # multiply size with y to get the right row and add x to move along
            row_total += board[y * size + x]
        # Equalling absolute value size means one type of counter only
        if row_total == size or row_total == -size:
            game_status = int(row_total / size)

    # check columns
    for x in range(size):
        column_total = 0
        for y in range(size):
            # for each value in column, add to total
            column_total += board[y * size + x]
        if column_total == size or column_total == -size:
            game_status = int(column_total / size)

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
    # Iterate over each line in the file
    for line in f:
        print(line.strip())
    f.close()


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

def get_int_input_in_range(prompt, min, max):
    valid_input = False
    first_guess = True
    while not valid_input:
        print(break_line)
        # Error message doesn't print first time through
        if first_guess:
            first_guess = False
        else:
            print("That is not a valid input. Please try again.")
        user_input = input(prompt)

        if is_digits_only(user_input):
            user_input = int(user_input)
            if min <= user_input <= max:
                valid_input = True
    return user_input


# ------------------------------------------------------------------------------#
#  is_digits_only(text)
# ------------------------------------------------------------------------------#
#  Purpose: Returns a boolean representing if the string passed to it is made
#  up of exclusively digits
# ------------------------------------------------------------------------------#
def is_digits_only(text):
    text = str(text)
    is_digits = True
    for i in range(len(text)):
        # checks each character to see if it's a digit
        if text[i] < "0" or text[i] > "9":
            is_digits = False
    # If string is empty it is not a valid int
    if text == "":
        is_digits = False
    return is_digits


main()
