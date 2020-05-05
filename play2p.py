from random import choice as chrand

def disp_board(board, nrow = 3, ncol = 3):
    """display the current status of the board"""
    print("  ", end = "")
    for j in range(ncol):
        print(f"{j + 1}", end = " ")
    print()
    for j in range(ncol + 1):
        print("--", end = "")
    print("-")
    for i in range(nrow):
        print("|", end = " ")
        for j in range(ncol):
            print(f"{board[i][j]}", end = " ")
        print(f"| {i + 1}")
    for j in range(ncol + 1):
        print("--", end = "")
    print("-")

def play2p(nrow = 3, ncol = 3, consec = 3):
    """
    to let two players play a game of tictactoe
    with a 3 x 3 game board with 3 consecutive symbols to be joined
    return the name of the winner
    """

    # two dictionaries to hold the players' info
    p = [{}, {}]
    print("Player 1, what is your name?")
    p[0]["name"] = input()
    print("Player 2, what is your name?")
    p[1]["name"] = input()
    
    # allocation of symbols to the players
    print("Tossing a coin to decide who chooses the symbol...")
    k = chrand([0, 1])
    print(f"{p[k]['name']} chooses the symbol. So what do you choose - X or O?")
    while True:
        sym = input()
        if sym.upper() == "X" or sym.upper() == "O":
            break
        print("Invalid choice. Enter X or O.")
    p[k]["sym"] = sym
    k = 0 if k else 1
    p[k]["sym"] = "X" if sym.upper() == "O" else "O"
    
    # the game board - a 2D array
    board = []
    for i in range(nrow):
        board.append([])
        for j in range(ncol):
            board[i].append(".")

    # who plays first?
    print("Tossing a coin to decide who takes the first turn...")
    k = chrand([0,1])

    # play until someone wins or the board is exhausted
    turn = 1 # keeping count of turns
    while turn <= ncol * nrow:
        print(f"Board at turn {turn}:\n")
        disp_board(board, nrow, ncol)

        print(f"{p[k]['name']} plays the turn {turn}.")

        # placing the symbols at the turn
        while True:
            coord = input().split("-")
            r, c = int(coord[0]), int(coord[1])
            if (r >= 1 and r <= nrow) and (c >= 1 and c <= ncol):
                if board[r - 1][c - 1] == ".":
                    board[r - 1][c - 1] = p[k]["sym"]
                    break
                else:
                    print("Occupied. Enter vacant coordinates.")
            else:
                print("Out of bounds. Enter valid coordinates.")

        # checking for victory along rows
        for i in range(nrow):
            for j in range(ncol - consec + 1):
                sym = board[i][j]
                if sym == ".":
                    continue
                l = 0
                while l < consec :
                    if board[i][j + l] != sym:
                        break
                    l += 1
                if l == consec:
                    winner = p[k]["name"] if sym == p[k]["sym"] else p[0 if k else 1]["name"]
                    return winner

        # checking for victory along columns
        for j in range(ncol):
            for i in range(nrow - consec + 1):
                sym = board[i][j]
                if sym == ".":
                    continue
                l = 0
                while l < consec:
                    if board[i + l][j] != sym:
                        break
                    l += 1
                if l == consec:
                    winner = p[k]["name"] if sym == p[k]["sym"] else p[0 if k else 1]["name"]
                    return winner

        # checking for victory along diagonals
        for i in range(nrow - consec + 1):
            # \ diagonals
            for j in range(ncol - consec + 1):
                sym = board[i][j]
                if sym == ".":
                    continue
                l = 0
                while l < consec:
                    if board[i + l][j + l] != sym:
                        break
                    l += 1
                if l == consec:
                    winner = p[k]["name"] if sym == p[k]["sym"] else p[0 if k else 1]["name"]
                    return winner

            # / diagonals
            for j in reversed(range(consec - 1, ncol)):
                sym = board[i][j]
                if sym == ".":
                    continue
                l = 0
                while l < consec:
                    if board[i + l][j - l] != sym:
                        break
                    l += 1
                if l == consec:
                    winner = p[k]["name"] if sym == p[k]["sym"] else p[0 if k else 1]["name"]
                    return winner

        k = 0 if k else 1
        turn += 1

    return "Draw: Both"
