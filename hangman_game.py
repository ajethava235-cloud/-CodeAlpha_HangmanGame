import random

WORDS = ["python", "hangman", "internship", "developer", "keyboard"]
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
      -----
      |   |
          |
          |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ---------
    """,
]

#Stage 0 → nothing
#tage 1 → head
#Stage 2 → body
#Stage 3 → one arm
#Stage 4 → second arm
#Stage 5 → one leg
#Stage 6 → second leg

def choose_word():
    """Randomly pick a word from the word list."""
    return random.choice(WORDS)


def display_state(word, guessed_letters, wrong_count):
    """Show the hangman drawing and the word with blanks."""
    print(HANGMAN_STAGES[wrong_count])
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word: " + display.strip())
    print("Guessed letters: " + ", ".join(sorted(guessed_letters)) if guessed_letters else "Guessed letters: none")
    print("Wrong guesses left: " + str(MAX_WRONG_GUESSES - wrong_count))


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_count = 0

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time. You have", MAX_WRONG_GUESSES, "wrong guesses allowed.\n")

    while wrong_count < MAX_WRONG_GUESSES:
        display_state(word, guessed_letters, wrong_count)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

        guess = input("\nGuess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            wrong_count += 1
            print("Wrong guess!\n")
        else:
            print("Good guess!\n")

    # If loop ends without winning
    print(HANGMAN_STAGES[wrong_count])
    print("You have been hanged! The word was:", word)

if __name__ == "__main__":
    play_hangman()