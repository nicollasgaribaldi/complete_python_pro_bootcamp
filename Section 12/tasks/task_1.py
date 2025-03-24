### NAMESPACES AND SCOPE

## Local Scope
# Variables (or functions) declared inside functions have local scope (also called function scope).
# They are only seen by other code within the same block of code.
# e.g.

# def my_function():
#     my_local_var = 2
    
# # This will cause a NameErrorr
# print(my_local_var) 

## Global Scope
# Variables or functions declared at the top level (unindented) of a code file have global scope.
# It is accessible anywhere in the code file.
# e.g.

# my_global_var = 3

# def my_function():
#     # This works no problems
#     print(my_global_var)

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope

# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)

# drink_potion()
# print(potion_strenght)

# Global Scope
player_health = 10 

def drink_potion():
    potion_strenght = 2
    print(player_health)

drink_potion()
print(player_health)
