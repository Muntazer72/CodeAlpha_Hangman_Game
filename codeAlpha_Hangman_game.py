import random

# List of 5 predefined words
Actual_words_List = ["apple", "brain", "chair", "dream", "eagle"]

# Choose a random word from the list
secret_word = random.choice(Actual_words_List)

# Initialize variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Create a display version of the word ("_ _ _ _ _")
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical letter.\n")
        continue

    if guess in guessed_letters:
        print("Warning... You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("Correct!\n")
    else:
        wrong_guesses += 1
        print(f"Incorrect! You have {max_wrong_guesses - wrong_guesses} guesses left.\n")

# Game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game Over! The word was:", secret_word)
