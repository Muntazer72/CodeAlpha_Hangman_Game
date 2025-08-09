# 🎮 CodeAlpha Hangman Game

A simple Hangman game implemented in Python as part of an internship task at **Code Alpha**. The game randomly selects a word from a predefined list, and the player attempts to guess it one letter at a time. The player has up to **6 incorrect guesses** before the game ends.


## 🕹️ How to Play

1. Run the Python script.
2. A series of underscores will appear, representing the secret word.
3. Enter one letter per guess.
4. Correct guesses reveal the letter(s) in the word.
5. Incorrect guesses reduce your remaining attempts.
6. The game ends when you either guess the word or run out of attempts.

## ✨ Features

- 🔀 Random word selection from a predefined list.
- ✅ Input validation (only single alphabetical letters allowed).
- 🔁 Prevents repeated guesses by tracking guessed letters.
- 🧩 Displays the current progress of the word after each guess.
- ❌ Limits the player to 6 incorrect guesses.

## 🧰 Requirements

- Python 3.x

## ▶️ How to Run

1. Ensure Python 3.x is installed on your system.
2. Save the script in a `.py` file (e.g., `hangman.py`).
3. Open a terminal or command prompt.
4. Run the script using:
   python hangman.py
### 💡 Sample Output
Welcome to Hangman!
Guess the word, one letter at a time.
You have 6 incorrect guesses.

Word: _ _ _ _ _
Guessed letters: 
Enter a letter: a
Correct!

Word: a _ _ _ _
Guessed letters: a
Enter a letter: e
Correct!

Word: a _ _ _ e
Guessed letters: a, e
Enter a letter: i
Incorrect! You have 5 guesses left.

Word: a _ _ _ e
Guessed letters: a, e, i
Enter a letter: p
Correct!

Word: a p p _ e
Guessed letters: a, e, i, p
Enter a letter: l
Correct!

Word: a p p l e
Guessed letters: a, e, i, p, l

 Congratulations! You guessed the word: apple
