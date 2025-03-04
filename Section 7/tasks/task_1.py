### HANGMAN ###

# Your goal is to build a Hangman game using everything you have learnt about Python programming.

## STEP 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

import random
chosen_word = random.choice(word_list) # Escolhe a palavra da lista
print(chosen_word) # Exibe a palavra escolhida

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = str(input('Choose a letter ').lower()) # Recebe uma letra e transforma no diminutivo
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')



