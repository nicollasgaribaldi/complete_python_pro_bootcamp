### HIGHER OR LOWER PROJECT ###

# The goal is to build a game that asks the user to guess who has more followers on Instagram.

# Original Higher Lower Game
# https://www.higherlowergame.com/

# Demo of Final Project
# https://appbrewery.github.io/python-day14-demo/

### HIGHER OR LOWER PROJECT ###

import random
from art import logo, vs
from game_data import data

def higher_or_lower():
    print(logo)
    
    score = 0
    data_a = random.choice(data)
    
    while True:
        data_b = random.choice(data)
        
        while data_b == data_a:
            data_b = random.choice(data)
        
        comp_1 = data_a['follower_count']
        comp_2 = data_b['follower_count']

        print(f"\nChoice A: {data_a['name']}, {data_a['description']}, {data_a['country']}.")
        print(vs)
        print(f"Choice B: {data_b['name']}, {data_b['description']}, {data_b['country']}.")

        choice = input("Who has more followers: A or B? ").strip().lower()

        if choice == "a" and comp_1 >= comp_2:
            score += 1
            data_a = data_b
            print(f"Correct! Your score is now {score}.")
        elif choice == "b" and comp_2 >= comp_1:
            score += 1
            data_a = data_b
            print(f"Correct! Your score is now {score}.")
        elif choice in ["a", "b"]:
            print(f"Wrong! Final score: {score}.")
            break 
        else:
            print("Invalid input. Please choose 'A' or 'B'.")
    
higher_or_lower()
