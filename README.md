# Connect4Game
# 420-942-VM: Application Development 1: Desktop

## Assignment 1: Connect 4 Game in Python

### Objective

Develop a console version of "Connect 4" in Python. This practical assignment will help you familiarize yourself with
Python's syntax and basic concepts, without using Android-specific features.

### Game Description

Connect 4 is a strategy game for two players. The goal is to align 4 tokens of your color horizontally, vertically, or
diagonally on a 6-row by 7-column grid.

### Required Features

1. Display the game grid in the console
2. Allow players to place their tokens in turns
3. Check for victory after each move
4. Handle errors (e.g., full column, invalid input)
5. Offer to play again at the end

### Project Structure

Here's the basic project structure with starter code:

```python
# File: game.py
# Name: <YOUR NAME>
# Student ID: <YOUR STUDENT ID>

class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def play(self):
        # TODO: Implement main game logic
        pass

    def display_board(self):
        # TODO: Display game grid
        pass

    def make_move(self, column):
        # TODO: Place a token in the specified column
        pass

    def check_win(self):
        # TODO: Check if there's a winner
        pass

    def is_board_full(self):
        # TODO: Check if the grid is full
        pass

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_board_cell(self, row, col):
        return self.board[row][col]

    def get_current_player(self):
        return self.current_player


# File: main.py
# Name: <YOUR NAME>
# Student ID: <YOUR STUDENT ID>

from game import Game

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
```

### Unit Tests

Here are some unit tests using the `unittest` module:

```python
# File: test_game.py
# Name: <YOUR NAME>
# Student ID: <YOUR STUDENT ID>

import unittest
from game import Game


class TestGame(unittest.TestCase):

    def test_initial_board_is_empty(self):
        game = Game()
        for row in range(6):
            for col in range(7):
                self.assertEqual(' ', game.get_board_cell(row, col))

    def test_make_valid_move(self):
        game = Game()
        self.assertTrue(game.make_move(3))
        self.assertEqual('X', game.get_board_cell(5, 3))

    def test_make_invalid_move(self):
        game = Game()
        self.assertFalse(game.make_move(7))  # Invalid column
        self.assertFalse(game.make_move(-1))  # Invalid column

    def test_make_move_in_full_column(self):
        game = Game()
        for _ in range(6):
            game.make_move(0)
        self.assertFalse(game.make_move(0))

    def test_switch_player(self):
        game = Game()
        self.assertEqual('X', game.get_current_player())
        game.switch_player()
        self.assertEqual('O', game.get_current_player())
        game.switch_player()
        self.assertEqual('X', game.get_current_player())

    def test_check_win_horizontal(self):
        game = Game()
        for col in range(4):
            game.make_move(col)
            if col < 3:
                game.switch_player()
                game.make_move(col)
                game.switch_player()
        self.assertTrue(game.check_win())

    def test_check_win_vertical(self):
        game = Game()
        for _ in range(4):
            game.make_move(0)
            if _ < 3:
                game.switch_player()
                game.make_move(1)
                game.switch_player()

        self.assertTrue(game.check_win())

    def test_check_win_diagonal_ascending(self):
        game = Game()
        moves = [(0, 'X'), (1, 'O'), (1, 'X'), (2, 'O'), (2, 'X'), (3, 'O'), (2, 'X'), (3, 'O'), (3, 'X'), (0, 'O'),
                 (3, 'X')]
        for col, player in moves:
            game.current_player = player
            game.make_move(col)
        self.assertTrue(game.check_win())

    def test_check_win_diagonal_descending(self):
        game = Game()
        moves = [(3, 'X'), (2, 'O'), (2, 'X'), (1, 'O'), (1, 'X'), (0, 'O'), (1, 'X'), (0, 'O'), (0, 'X'), (3, 'O'),
                 (0, 'X')]
        for col, player in moves:
            game.current_player = player
            game.make_move(col)
        self.assertTrue(game.check_win())

    def test_no_win_yet(self):
        game = Game()
        game.make_move(0);
        game.switch_player();
        game.make_move(1)
        game.switch_player();
        game.make_move(2);
        game.switch_player();
        game.make_move(3)
        self.assertFalse(game.check_win())

    def test_is_board_full_when_full(self):
        game = Game()
        for col in range(7):
            for _ in range(6):
                game.make_move(col)
        self.assertTrue(game.is_board_full())

    def test_is_board_full_when_not_full(self):
        game = Game()
        game.make_move(0);
        game.switch_player();
        game.make_move(1)
        self.assertFalse(game.is_board_full())


if __name__ == '__main__':
    unittest.main()
```

### Instructions

1. Create a Python project in PyCharm.
2. Complete the functions in the `Game` class.
3. Implement game logic in the `play()` function.
4. Ensure the game properly handles user input.
5. Ensure all unit tests pass.
6. Comment your code clearly and concisely.
    - At the beginning of each Python file, write your name and student ID in a comment.
7.  Create a git repository for your project and share it on GitHub with user *profdenis*.


### Evaluation Criteria

- Complete game functionality (50%)
- Code quality and structure (30%)
- Unit tests (10%)
- Error handling and edge cases (10%)

### Due Date: Sunday May 4th before midnight
