# https://reeborg.ca/reeborg.html

### Hurdles race  ###

# Reeborg has entered a hurdle race. Make him run the course, following the path shown.

# The position, the height and the number of hurdles changes each time this world is reloaded.

## What you need to know
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.

# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

## Difficulty level IV 1/2

# Background image: www.pexels.com

# A robot located at (x, y) = (1, 1) carries no objects.

## Goal to achieve:
# The final position of the robot must be (x, y) = (13, 1)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def salto():
    turn_right()
    move()
    turn_right()

while not at_goal():
    if wall_in_front():
        turn_left()
    else:
        move()
    if right_is_clear():
        salto()
