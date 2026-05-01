import random

secret_number = random.randint(1, 10)

print("Welcome to Number Guessing Game!")
print("I have chosen a number between 1 and 10.")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Congratulations! You guessed it right.")
else:
    print("Sorry! The correct number was", secret_number)