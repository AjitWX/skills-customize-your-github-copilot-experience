
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build an interactive Hangman game using Python control flow, string operations, collections, and user input handling. Students will practice game state tracking and user feedback loops while applying validation and loop logic.

## 📝 Tasks

### 🛠️ Implement Hangman Core Game

#### Description

Write a `hangman()` function (or script) that runs a complete Hangman playthrough from word selection through win/lose resolution.

#### Requirements

Completed program should:
- Use a predefined list of words and randomly select one word with `random.choice()`.
- Display the hidden word progress as underscores and correctly guessed letters (e.g., `p _ t h o n`).
- Prompt the player to guess one letter at a time using `input()`.
- Track and display incorrect guesses remaining (e.g., 6 attempts max).
- Prevent counting duplicate guesses against remaining attempts.
- End the game with a win message when the word is fully guessed.
- End the game with a loss message when attempts are exhausted.

### 🛠️ Add Player Feedback and Replay

#### Description

Extend the game to provide real-time feedback and support replaying.

#### Requirements

Completed program should:
- Show a list of guessed letters (correct and incorrect) after each turn.
- Display a clear message for invalid input (e.g., if input is not a single alphabet character or has already been guessed).
- After game over, ask the player if they want to play again (`y`/`n`).
- Reset game state correctly if the player chooses to replay.

