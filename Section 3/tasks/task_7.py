### TREASURE ISLAND PROJECT ###

# Your goal today is to build a "Chose your own adventure game".
# Using what you have learnt in the lessons today you will be building a very simple version of
# this type of text game.

# Use the flow chart linked here to create the game logic.
# Once you've completed the project, you can always extend the game and make it more interesting!

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

decision_1 = input('You\'re at a crossroad, where do you want to go?\n'
                   'Type "left" or "right".\n').lower()

if decision_1 == "left":
    decision_2 = input('You\'ve come to a lake. '
                  'There is a island in the middle of the lake. \n'
                  'Type "wait" to wait for a boat. '
                  'Type "swin" to swin across.\n').lower()
    if decision_2 == "wait":
        decision_3 = input('You arrive at the island unharmed.\n'
                           'There is house with 3 doors. One red, '
                           'one yellow and one blue.\n'
                           'Which colour do you choose?\n').lower()
        if decision_3 == "red":
            print('It\'s a room full of fire.\nGame over!')
        elif decision_3 == "yellow":
            print('You found the treasure.\nYou win!')
        elif decision_3 == "blue":
            print('You enter a room of beasts. Game over!')
        else:
            print('You chose a door that doesn\'t exist.\nGame over!')
    else:
        print('You got attacked by an angry trout.\nGame over!')
else:
     print('You fell into a hole. Game over!')