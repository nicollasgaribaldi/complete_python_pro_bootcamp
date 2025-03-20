### CALCULATOR PROJECT ###

# The goal is to build a calculator program.

## Demo
# https://appbrewery.github.io/python-day10-demo/

## Storing Functions as a Variable Value
# You can store a reference to a function as a value to a variable. e.g.

# def add(n1, n2):
#     return n1 + n2
    
    
# my_favourite_calculation = add
# my_favourite_calculation(3, 5)  # Will return 8
# In the starting file, you'll see a dictionary that references each of the mathematical calculations that can be performed by our calculator. Try it out and see if you can get it to perform addition, subtraction, multiplication and division.

## PAUSE 1
# TODO: Write out the other 3 functions - subtract, multiply and divide.

## PAUSE 2
# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

## PAUSE 3
# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

## Functionality
    # Program asks the user to type the first number.
    # Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
    # Program asks the user to type the second number.
    # Program works out the result based on the chosen mathematical operator.
    # Program asks if the user wants to continue working with the previous result.
    # If yes, program loops to use the previous result as the first number and then repeats the calculation process.
    # If no, program asks the user for the fist number again and wipes all memory of previous calculations.
    # Add the logo from art.py

#  Hint 1 
# Try writing out a flowchart to plan your program.
#  Hint 2 
# To call multiplication from the operations dictionary, you would write your code like this:
# result = operations["*"](n1= 5, n2= 3)

# result would then be equal to 15.

import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide
}

def calculator():
  print(art.logo)
  should_accumulate = True
  n1 = float(input("What\'s the first number? "))

  while should_accumulate:
    for symbol in operations:
      print(symbol)
    operation = input("Pick an operation: ")
    n2 = float(input("What\'s the next number? "))
    result = operations[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    
    choice = input(f"Type 'y' to continue operating with {result}, or type 'n' to start a new calculation: ")
    
    if choice == 'y':
      n1 = result
    else:
      should_accumulate = False
      print("\n" * 20)
      calculator()

calculator()
