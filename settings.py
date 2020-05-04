# to capture the settings of the game as Settings object

from math import sqrt

class Settings:
    """
    a class to create an object to
    store the settings of tictactoe game
    """

    def __init__(self):
        """give the default states of settings"""
        self.nrow = 3 # number of rows in the board
        self.ncol = 3 # number of columns in the board
        self.consec = 3 # number of consecutive symbols to be joined to win
        self.players = 2 # number of players

    def change_settings(self):
        """the change settings menu"""
        opt = 0
        while opt != 5:
            print("You can change the settings of the following parameters.")
            print("Choose an option 1 - 5.")
            print("1. Number of rows in the board. (default 3)")
            print("2. Number of columns in the board. (default 3)")
            print("3. Number of consecutive symbols to be joined to win. (default 3)")
            print("4. Number of players playing the game. (1 or 2; default 2)")
            print("5. Exit settings menu.")
            opt = int(input())

            if opt == 1:
                print("Enter the new number of rows.")
                self.nrow = int(input())

            elif opt == 2:
                print("Enter the new number of columns.")
                self.ncol = int(input())
            
            elif opt == 3:
                print("Enter the new number of consecutive symbols to win.")
                self.consec = int(input())

            elif opt == 4:
                print("Enter the new number of players.")
                self.players = int(input())

            elif opt != 5:
                print("Invalid choice.")

    def validate_settings(self):
        """check if the settings make sense before starting the game"""
        if self.nrow <= 0 or self.ncol <= 0 or self.consec <= 0 or self.players <= 0:
            return False
        elif self.consec > sqrt(self.ncol ** 2 + self.nrow ** 2):
            return False
        elif self.players > 2:
            return False
        return True
