# main.py
import random
from view import GameView
from game_controller import GameController

def main():
    """Entry point of the game"""
    view = GameView()
    game = GameController(view)
    game.run()

if __name__ == "__main__":
    main()