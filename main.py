# File: main.py
# Name: <Kristina Cecura>
# Student ID: <2495184>
from game import Game

def main():
    while True:
        game = Game()
        game.play()

        replay = input("Play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing Connect 4!")
            break

if __name__ == "__main__":
    main()
