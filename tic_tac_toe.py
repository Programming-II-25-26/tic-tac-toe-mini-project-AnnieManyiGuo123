# https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/

def instructions():
    print("Welcome to Noughts and Crosses!")
    print("-------------------------------")
    print("Instructions:")
    print("This is a 2 player game.")
    print("The first player will be noughts.")
    print("The second player will be crosses.")
    print("The game is presented in a grid...")
    print("""
     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
    """)
    print("To choose a position for your piece, enter the location number.")
    print("Player X goes first.")


def displayboard(board):
    print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
    print(" ───┼───┼───")
    print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
    print(" ───┼───┼───")
    print(" ", board[2][0], "│", board[2][1], "│", board[2][2])


def check_win(board, player):
    # list all possibilities of win
    won = False
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        won = True
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        won = True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        won = True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        won = True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        won = True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        won = True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        won = True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        won = True
    return won


def checkpositions():
    # valid = 1-9 (make sure they are string)
    # map (); str()
    valid = list(map(str, range(1, 10)))
    pos = input("Enter a position (1-9): ")
    while pos not in valid:
        pos = input("You must enter a number from 1-9: ")
    # transfer to int 
    # dont forget -1, since start at 0
    return int(pos) - 1


def move(board, player):
    pos = checkpositions()
    # the calculation to transfer "1-9" to "0,1,2"
    row = pos // 3
    col = pos % 3

    # resource: https://www.w3schools.com/python/ref_string_isdigit.asp [isdigit()]
    while not board[row][col].isdigit():  
        print("That spot is already taken. Try again.")
        pos = checkpositions()
        row = pos // 3
        col = pos % 3

    board[row][col] = player
    return board


def play(board):
    # initial; out of the while
    currentplayer = "X"

    while True:
        displayboard(board)
        print(f"{currentplayer}'s turn. Where would you like to place your piece?")
        move(board, currentplayer)

        if check_win(board, currentplayer):
            displayboard(board)
            print(f" Player {currentplayer} wins! ")
            break
        
        # if no one win
        # check cell blank; board_full = false
        board_full = True
        for row in board:
            for cell in row:
                if cell.isdigit():
                    board_full = False
                    break
            if not board_full:
                break

        if board_full:
            displayboard(board)
            print("No one win!")
            break


        if currentplayer == "X":
            currentplayer = "O"
        else:
            currentplayer = "X"


if __name__ == "__main__":
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    # run
    instructions()
    play(board)
