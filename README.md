
# Hangman Game — CodeAlpha Python Internship Task 1

A simple text-based Hangman Game built with Python as part of the CodeAlpha Python Programming Internship.

---

#  Project Overview

The player tries to guess a hidden word one letter at a time.
Each wrong guess brings the player closer to losing the game.
The game ends when the player either guesses the word correctly or runs out of attempts.

---

#  Features

* 🔤 5 randomly selected predefined words
* 💀 ASCII art hangman displayed after wrong guesses
* ✅ Tracks guessed letters
* 🔁 Play again option
* 🖥️ Simple console-based game
* 📦 No external libraries required

---

#  Technologies Used

* **Language:** Python 3

* **Concepts:**

  * random module
  * while loops
  * if-else conditions
  * strings
  * lists
  * sets

* **Libraries:** Built-in Python libraries only

---

# How to Run

## 1. Install Python 3

Make sure Python 3 is installed on your system.

## 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_HangmanGame.git
```

## 3. Navigate to the Project Folder

```bash
cd CodeAlpha_HangmanGame
```

## 4. Run the Game

```bash
python hangman_game.py
```

---

#  How to Play

1. Run the Python file
2. A random word will appear as underscores (`_ _ _ _`)
3. Guess one letter at a time
4. Each wrong guess increases the hangman drawing
5. You lose after 6 wrong guesses
6. Guess the complete word to win 🎉

---

#  Sample Output

```text
========================================
       Welcome to HANGMAN!
========================================

       -----
       |   |
           |
           |
           |
           |
    =========

Word: _ _ _ _ _ _
Wrong guesses left: 6

Guess a letter: p
'p' is in the word!

Word: p _ _ _ _ _
Guess a letter: z
 'z' is NOT in the word.
```

---

#  Project Structure

CodeAlpha_HangmanGame/
│
├── hangman_game.py
└── README.md


---

# 👨‍💻 Author

* **Name:** Maha Faheem Bhatti
* **Internship:** CodeAlpha Python Programming Internship
* **LinkedIn:** Your LinkedIn Profile
* **GitHub:** Your GitHub Profile

---

