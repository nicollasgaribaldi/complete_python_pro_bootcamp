# https://reeborg.ca/reeborg.html

### Hurdles race  ###

# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position and number of hurdles changes each time this world is reloaded.

## What you need to know
    # The functions move() and turn_left().
    # The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
    # How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

## Difficulty level IV
# Background image: www.pexels.com

# A robot located at (x, y) = (1, 1) carries no objects.

## Goal to achieve:
# The final position of the robot must be (x, y) = (13, 1)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def salto():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        salto()
