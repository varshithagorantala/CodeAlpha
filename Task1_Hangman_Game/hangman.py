import random

# Predefined list of 5 words
words = ["python", "apple", "computer", "banana", "coding"]

# Randomly select a word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
attempts = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if letter already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guessed letter is in word
    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong Guess!")
        attempts -= 1

# Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)