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

def play1p(nrow = 3, ncol = 3, consec = 3):
    """
    to let two players play a game of tictactoe
    with a 3 x 3 game board with 3 consecutive symbols to be joined
    return the name of the winner
    """
    
    # a list of 2 dictionaries to hold the players
    p = [{}, {}]
    print("Player 1, what is your name?")
    p[0]["name"] = input()
    print("Player 2 is the computer - 'Lord of Probability'.")
    p[1]["name"] = "Lord of Probability"
    
    # allocation of symbols to the players
    print("Tossing a coin to decide who chooses the symbol...")
    k = chrand([0, 1])
    print(f"{p[k]['name']} chooses the symbol. So what do you choose - X or O?")
    if k == 0:
        while True:
            sym = input()
            if sym.upper() == "X" or sym.upper() == "O":
                break
            print("Invalid choice. Enter X or O.")
    else:
        sym = chrand(["X", "O"])
        print(f"I choose {sym}")
    p[k]["sym"] = sym
    k = 0 if k else 1
    p[k]["sym"] = "X" if sym.upper() == "O" else "O"
    
    # board is 2D array to hold the current status of the playing board
    board = []
    for i in range(nrow):
        board.append([])
        for j in range(ncol):
            board[i].append(".")

    # deciding who plays first
    print("Tossing a coin to decide who takes the first turn...")
    k = chrand([0,1])

    # playing until we run out of the board or someone wins
    turn = 1 # the turn number
    while turn <= ncol * nrow:
        print(f"Board at turn {turn}:\n")
        disp_board(board, nrow, ncol)

        print(f"{p[k]['name']} plays the turn {turn}.")
        while True:
            if k == 0:
                coord = input().split("-")
                r, c = int(coord[0]), int(coord[1])
            else:
                r = chrand(range(nrow)) + 1
                c = chrand(range(ncol)) + 1

            if (r >= 1 and r <= nrow) and (c >= 1 and c <= ncol):
                if board[r - 1][c - 1] == ".":
                    board[r - 1][c - 1] = p[k]["sym"]
                    break
                else:
                    if k == 0:
                        print("Occupied. Enter vacant coordinates.")
            else:
                if k == 0:
                    print("Out of bounds. Enter valid coordinates.")
        
        # checking along for victory along rows
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
            # checking for victory along \ diagonals
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

            # checking for victory along / diagonals
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
