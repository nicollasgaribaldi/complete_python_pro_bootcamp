### NUMBER GUESSING PROJECT ###

# The goal is to build a guess the number game.

## Demo
# https://appbrewery.github.io/python-day12-demo/

## ASCII Art
# You can get hold of ASCII art using the link below: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

def guessing_game():
    random_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("That difficulty doesn't exist.")
        return 

    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == random_number:
            print("Você acertou, danadinho! 🎉")
            return
        elif guess > random_number:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print("You've run out of attempts. You lose!")
            print(f"The correct number was {random_number}.")

guessing_game()
