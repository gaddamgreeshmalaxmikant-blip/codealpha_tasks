import random


def hangman():
    # Predefined list of words
    words = ["python", "hangman", "programming", "computer", "keyboard"]

    # Select a random word
    secret_word = random.choice(words)

    # Game variables
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_progress = ["_"] * len(secret_word)

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print("You can have up to", max_incorrect_guesses, "incorrect guesses.")

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses and "_" in word_progress:
        # Display current game state
        print("\nWord: " + " ".join(word_progress))
        print("Guessed letters: " + ", ".join(guessed_letters))
        print("Incorrect guesses remaining:", max_incorrect_guesses - incorrect_guesses)

        # Get player's guess
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        # Add to guessed letters
        guessed_letters.append(guess)

        # Check if guess is in the secret word
        if guess in secret_word:
            print("Good guess!")
            # Update word progress
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    word_progress[i] = guess
        else:
            print("Sorry, that letter is not in the word.")
            incorrect_guesses += 1

    # Game over - check win/lose condition
    if "_" not in word_progress:
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print("\nGame over! The word was:", secret_word)


# Start the game
if __name__ == "__main__":
    hangman()