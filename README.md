# 🎯 Number Guessing Game (Python)

A simple and fun number guessing game built with Python. The computer randomly selects a secret number, and the player tries to guess it within as few attempts as possible.

## 🚀 Features

- Random secret number generation
- Custom lower and upper number limits
- Hints for guesses that are too high or too low
- Counts the total number of attempts
- Displays a congratulatory message when the correct number is guessed

## 🛠️ Technologies Used

- **Language:** Python
- **Module:** `random` (Python standard library)

## 📋 Requirements

- Python 3.x
- Any code editor, such as Visual Studio Code

## ▶️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/programmer-nazmul19/number-gueass-game.git
   ```

2. Open the project folder:

   ```bash
   cd number-guess-game
   ```

3. Run the Python file:

   ```bash
   python main.py
   ```

   Replace `main.py` with your actual Python filename if it is different.

## 🎮 How to Play

1. Enter the lower number.
2. Enter the upper number.
3. Guess the secret number.
4. Follow the hints:
   - **Too low!** — Try a higher number.
   - **Too high!** — Try a lower number.
5. Keep guessing until you find the correct number.
6. Try to win in as few attempts as possible!

## 📸 Example Output

```text
Enter the lower number: 1
Enter the upper number: 10
This is a number guessing game.
Guess the secret number between 1 and 10.
Try to guess the number in as few attempts as possible.
Enter your guess: 5
Too low! Try again.
Enter your guess: 8
Congratulations! You guessed the secret number 8.
You guessed the number in 2 attempts.
```

*Note: The example output may vary because the secret number is generated randomly.*

## 📚 What I Learned

- Using Python's `random` module
- Taking user input with `input()`
- Converting input into integers with `int()`
- Using `while` loops and conditional statements
- Tracking attempts with a counter
- Using `f-strings` to format output

## 👨‍💻 Author

Created as a Python programming practice project.

## 📄 License

This project is open source and available for learning and educational purposes.
