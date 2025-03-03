# https://reeborg.ca/reeborg.html

### Hurdles race  ###

# Reeborg has entered a hurdles race. Make him run the course, following the path shown.

## What you need to know
    # The functions move() and turn_left().

## Difficulty level I

## More advanced
# You may have noticed that your solution has some repeated patterns.
# If you know how to define functions, define a function named jump() and use it to simplify your program.

## Difficulty level II

# Background image: www.pexels.com

# A robot located at (x, y) = (1, 1) carries no objects.

## Goal to achieve:
# The final position of the robot must be (x, y) = (13, 1)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def salto():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

salto()
salto()
salto()
salto()
salto()
salto()
