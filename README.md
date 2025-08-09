# CodeAlpha_Hangman_Game
A simple Hangman game implemented in Python as part of an internship task at Code Alpha. The game randomly selects a word from a predefined list, and the player tries to guess it one letter at a time. The player has up to 6 incorrect guesses before the game ends.
**How to Play**
1.	Run the Python script.
2.	You will see a series of underscores representing the secret word.
3.	Enter one letter per guess.
4.	Correct guesses reveal the letter(s) in the word.
5.	Incorrect guesses reduce the remaining attempts.
6.	The game ends when you either guess the word or run out of guesses.
**Features**
•	Random word selection from a fixed list.
•	Input validation (only single alphabetical letters allowed).
•	Tracks guessed letters and prevents repeated guesses.
•	Displays the current progress of the word after each guess.
•	Limits the player to 6 wrong guesses.
**Requirements**
•	Python 3.x
**How to Run**
1.	Make sure Python is installed on your system.
2.	Save the script in a .py file, e.g., hangman.py.
3.	Run the script using the command:
   python hangman.py
4.	Follow the on-screen instructions to play.

### **Sample Output**

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

...

Congratulations! You guessed the word: apple
