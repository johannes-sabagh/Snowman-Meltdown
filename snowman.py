"""
Snowman Meltdown Game - Main Entry Point

This is the main module for the Snowman Meltdown word-guessing game.
It contains the word list used for the game and serves as the entry point
when the game is run as a script.

Game Overview:
    Snowman Meltdown is a word-guessing game where players try to guess a
    secret word letter by letter. Each incorrect guess causes the snowman
    to melt further. The goal is to guess all letters before the snowman
    completely melts away.
"""

import game_logic


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


# Entry point - only runs when this file is executed directly (not imported)
if __name__ == "__main__":

    while True:
        # Start the game
        game_logic.play_game()
        play_again = input("Please enter y to play again or any other key to exit: ")

        if play_again.casefold() ==  "y".casefold():
            continue
        else:
            print("Bye!")
            break
