"""
Game Logic Module for Snowman Meltdown

This module contains the core game logic for the Snowman word-guessing game.
Players must guess letters to reveal a hidden word before the snowman melts
completely. Each incorrect guess causes the snowman to melt further.

Functions:
    get_random_word: Randomly selects a word from the word list
    display_game_state: Shows the current game state with ASCII art and word progress
    play_game: Main game loop that handles user input and game flow
"""

import ascii_art
import random
import snowman


def get_random_word():
    """Selects a random word from the list."""
    return snowman.WORDS[random.randint(0, len(snowman.WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the ASCII Art stage and the word from the input accordingly """

    # Display the appropriate ASCII art stage based on number of mistakes
    print(ascii_art.STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    # Print the word progress
    print("Word: ", display_word)
    print("\n")


def play_game():
    """
    Main game engine that runs the Snowman Meltdown game loop.

    This function orchestrates the entire game flow:
    - Selects a random word for the player to guess
    - Tracks guessed letters and mistakes
    - Prompts the user for letter guesses
    - Updates and displays the game state after each guess
    - Determines win/loss conditions and ends the game appropriately

    The game ends when either:
    - The player guesses all letters correctly (win)
    - The player makes too many mistakes and the snowman melts (loss)
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    # Display the initial game state.
    display_game_state(mistakes, secret_word, guessed_letters)

    # Prompt user for guesses as long as the mistakes are less than 4 (the number of art stages)
    # Main game loop - continue until win or loss condition is met
    while mistakes <= len(secret_word):
        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            guessed_letters.append(guess)
            display_game_state(mistakes, secret_word, guessed_letters)

            # Check for win condition - all unique letters have been guessed
            if len(guessed_letters) == len(secret_word):
                print("Congratulations, you saved the snowman!")
                break
        else:
            display_game_state(mistakes, secret_word, guessed_letters)
            mistakes += 1

            # Check for loss condition - too many mistakes (snowman fully melted)
            if mistakes == len(ascii_art.STAGES):
                print(f"Game Over! The word was: {secret_word}")
                break
