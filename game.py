# a 3x3 tictactoe game
# designed for 2 players

import json
from play1p import play1p
from play2p import play2p
from settings import Settings

def give_choices(choices, obj, excluded = ""):
    """to accept a user action except for the excluded action"""

    print("Enter one of the following.")
    for key in choices.keys():
        if excluded == "" or excluded != key:
            print(f"{key}: {choices[key]}")
    action = input().upper() # choice chosen

    # exit the game
    if action == "E":
        quit()

    # read instructions
    elif action == "I":
        filename = "instructions.txt" # instructions for the game
        print("-----------------------------------------")
        with open(filename) as f:
            for line in f:
                print(line, end = "")
        print("-----------------------------------------\n")
        give_choices(choices, obj, "I")

    # play the game, that is, continue on the main course
    elif action == "C":
        print("----------------------------------------")
        if not obj.validate_settings():
            print("Invalid settings.")
            obj.change_settings()
            give_choices(choices, obj)

        if obj.players == 1:
            winner = play1p(obj.nrow, obj.ncol, obj.consec)

        else:
            winner = play2p(obj.nrow, obj.ncol, obj.consec)

        print(f"{winner} wins!")
        print("----------------------------------------\n")
        give_choices(choices, obj)

    # change settings
    elif action == "S":
        print("---------------------------------------")
        obj.change_settings()
        print("---------------------------------------\n")
        give_choices(choices, obj)

    else:
        print("Invalid choice. Please choose a valid action.")
        give_choices(choices, obj)

print("Hello! Welcome to the TicTacToe game.\n")

filename = "choices.json" # a file storing the choices menu for the game
with open(filename) as f:
    choices = json.load(f) # dictionary to hold the choices

obj = Settings() # settings object for game settings
give_choices(choices, obj)
