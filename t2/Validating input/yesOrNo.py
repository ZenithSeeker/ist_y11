

def yesOrNo(text):
    print(text)
    dec = input("Please enter with [y/n]: ")
    while dec.upper() != "Y" and dec.upper() != "N":
        dec = input("Please enter with [y/n]: ")
    if dec.upper() == "Y":
        choice = True
    else:
        choice = False
    return choice

def hello():
    board = [""] * 10
    de(board)
    prin(board)

def de(board):
    board[4] = "s"

def prin(board):
    print(board)

hello()