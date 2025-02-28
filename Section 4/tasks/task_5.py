### ROCK PAPER SCISSORS ###

# You are going to build a Rock, Paper, Scissors game.
# You will need to use what you have learnt about randomisation and Lists to achieve this.

## Demo
# https://appbrewery.github.io/python-day4-demo/

import random

# Opções de escolha
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Criando lista de opções
list = [rock, paper, scissors]

# Recebendo escolha do jogador
choice = int(input('What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors\n'))
if choice >= 0 and choice <= 2:
    print(f'You chose:\n{list[choice]}')

# Gerando escolha randomica do computador
computer_choice = random.randint(0, 2)
print(f'Computer chose:\n{list[computer_choice]}')

# Comparando e exibindo resultado
if choice >= 3:
    print('You typed a wrong number. Restart.')
elif choice == 0 and computer_choice == 1:
    print('You lose.')
elif choice == 0 and computer_choice == 2:
    print('You win!')
elif choice == 1 and computer_choice == 0:
    print('You win!')
elif choice == 1 and computer_choice == 2:
    print('You lose')
elif choice == 2 and computer_choice == 0:
    print('You lose')
elif choice == 2 and computer_choice == 1:
    print('You win!')
else:
    print('It\'s a draw;')
