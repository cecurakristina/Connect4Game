# File: game.py
# Name: <Kristina Cecura>
# Student ID: <2495184>
class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def play(self):
        # TODO: Implement main game logic
        game_over = False

        while not game_over:
            self.display_board()
            
            try:
                column = int(input(f"Player {self.current_player}, choose a column (0-6): "))
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 6.")
                continue

            if not self.make_move(column):
                print("Column full or invalid. Try again.")
                continue

            if self.check_win():
                self.display_board()
                print(f"Player {self.current_player} wins!")
                game_over = True
            elif self.is_board_full():
                self.display_board()
                print("It's a tie!")
                game_over = True
            else:
                self.switch_player()

    def display_board(self):
        # TODO: Display game grid
        print("\n 0 1 2 3 4 5 6") 
        print("-----------------")
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print("-----------------\n")

    def make_move(self, column):
        # TODO: Place a token in the specified column
        if column < 0 or column >= 7:
            return False 

        for row in range(5, -1, -1): 
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return True
            
        return False

    def check_win(self):
        # TODO: Check if there's a winner
        # Check horizontal win
        for row in range(6):
            for col in range(4):
                if (self.board[row][col] == self.current_player and
                    self.board[row][col + 1] == self.current_player and
                    self.board[row][col + 2] == self.current_player and
                    self.board[row][col + 3] == self.current_player):
                    return True

        # Check vertical win
        for col in range(7):
            for row in range(3):
                if (self.board[row][col] == self.current_player and
                    self.board[row + 1][col] == self.current_player and
                    self.board[row + 2][col] == self.current_player and
                    self.board[row + 3][col] == self.current_player):
                    return True

        # Check diagonal (bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if (self.board[row][col] == self.current_player and
                    self.board[row - 1][col + 1] == self.current_player and
                    self.board[row - 2][col + 2] == self.current_player and
                    self.board[row - 3][col + 3] == self.current_player):
                    return True

        # Check diagonal (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == self.current_player and
                    self.board[row + 1][col + 1] == self.current_player and
                    self.board[row + 2][col + 2] == self.current_player and
                    self.board[row + 3][col + 3] == self.current_player):
                    return True

        return False

    def is_board_full(self):
        # TODO: Check if the grid is full
        for col in range(7):
            if self.board[0][col] == ' ':
                return False
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_board_cell(self, row, col):
        return self.board[row][col]

    def get_current_player(self):
        return self.current_player
