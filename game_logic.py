import ascii_art
import random
import snowman


def get_random_word():
    """Selects a random word from the list."""
    return snowman.WORDS[random.randint(0, len(snowman.WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(ascii_art.STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.
    display_game_state(mistakes, secret_word, guessed_letters)

    # Prompt user for one guess (logic to be enhanced later)
    while mistakes <= len(secret_word):
        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            guessed_letters.append(guess)
            display_game_state(mistakes, secret_word, guessed_letters)
            if len(guessed_letters) == len(secret_word):
                print("Congratulations, you saved the snowman!")
                break
        else:
            display_game_state(mistakes, secret_word, guessed_letters)
            mistakes += 1
            if mistakes == len(ascii_art.STAGES):
                print(f"Game Over! The word was: {secret_word}")
                break
