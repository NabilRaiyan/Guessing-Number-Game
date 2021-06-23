import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 to 100.")
# Asking for difficulty level
difficulty = input("Choose the difficulty. Type 'easy' or 'hard'.\nEnter: ").lower()
random_number = random.randint(1, 101)

attempts_remaining = 1
attempts = 0

"""Function for checking the answer"""


def check():
    # Loop for continue asking user for input and checking for the right guess
    global attempts
    while attempts >= attempts_remaining:
        guess = int(input("Make a guess: "))
        if guess > random_number:
            attempts -= 1
            print("Too high!")
            print(f"You have {attempts} remaining to guess the number.")
            if attempts < attempts_remaining:
                print(f"Oh!You lose. The number was {random_number}.")
        elif guess < random_number:
            attempts -= 1
            print("Too low!")
            print(f"You have {attempts} remaining to guess the number.")
            if attempts < attempts_remaining:
                print(f"Oh!You lose. The number was {random_number}.")
        elif guess == random_number:
            attempts -= 1
            attempts = 0
            print(f"Congratulations! You got it.\nThe number was {random_number}")


if difficulty == "easy":
    attempts = 10
    check()
elif difficulty == "hard":
    attempts = 5
    check()
