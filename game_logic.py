import random
import ascii_art
import snowman

def get_random_word():
    """Selects a random word from the list."""
    return snowman.WORDS[random.randint(0, len(snowman.WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
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
    max_mistakes = len(ascii_art.STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    # Main game loop
    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check if player has won
        word_complete = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_complete = False
                break

        if word_complete:
            print("Congratulations! You saved the snowman!")

            return

        # Get player's guess
        guess = input("Guess a letter: ").lower()

        # Add guess to guessed letters
        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            continue
        else:
            mistakes += 1


    # Game over - player lost
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game Over! The word was: {secret_word}")



