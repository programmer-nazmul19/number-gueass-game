import random
lower_num = int(input("Enter the lower number: "))
upper_num = int(input("Enter the upper number: "))
secret_number = random.randint(lower_num, upper_num)
print("This is a number guessing game.")
print(f"Guess the secret number between {lower_num} and {upper_num}.")
print("Try to guess the number in as few attempts as possible.")
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_number}.")
        break
print(f"You guessed the number in {attempts} attempts.")
