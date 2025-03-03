# https://reeborg.ca/reeborg.html

### Hurdles race  ###

# Reeborg has entered a hurdle race, but he does not know in advance how long the race is.
# Make him run the course, following a path similar to the one shown,
# but stopping at the only flag that will be shown after the race has started.

## What you need to know
    # The functions move() and turn_left().
    # The condition at_goal() and its negation.
    # How to use a while loop.
# Your program should also be valid for world Hurdles 1.

## Difficulty level III

# Background image: www.pexels.com

# A robot located at (x, y) = (8, 2) carries no objects.

## Goal to achieve:
# The final position of the robot must be (x, y) = (11, 1)

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
    move()
    salto()
