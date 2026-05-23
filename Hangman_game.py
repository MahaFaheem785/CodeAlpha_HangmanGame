import random

WORDS = ["python", "rocket", "bridge", "jungle", "castle"]

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    print("=" * 40)
    print("       Welcome to HANGMAN!")
    print("=" * 40)

    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    while wrong_guesses < max_wrong:

        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

        if guessed_letters:
            print(f"Letters tried: {', '.join(sorted(guessed_letters))}")

        # Win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\nYou guessed it! The word was '{word}'.")
            break

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already tried that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    else:
        print(f"\n Game Over! The word was '{word}'.")

    again = input("\nPlay again? (yes/no): ").strip().lower()

    if again in ("yes", "y"):
        hangman()
    else:
        print("Goodbye and thanks for playing")

if __name__ == "__main__":
    hangman()