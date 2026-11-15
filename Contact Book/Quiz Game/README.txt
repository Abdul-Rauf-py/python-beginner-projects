# Quiz Game (Command Line)

A five-question general knowledge quiz you play in the terminal. The questions appear in a random order each time, and you type the full answer.

## Features
- 5 multiple-choice questions, shown with their options
- Question order is shuffled every game
- Answers are not case-sensitive ("paris" and "Paris" both count)
- Shows your final score at the end

## How to run
1. Install Python 3.12 or newer from python.org
2. Download `quiz_game.py`
3. Run: `python quiz_game.py`

No extra libraries are needed.

## How to play
Answer "yes" to start. Each question shows four options. Type the full answer (for example `Paris`, not `2`) and press Enter.

## What I practiced
- Storing questions as a list of dictionaries, with a list of options inside each
- Nested loops (questions, then options)
- The `random` module to shuffle the questions
- Keeping a running score

## Possible improvements
- Answer by option number instead of typing the full text
- Load questions from a file
- Show which questions were missed at the end