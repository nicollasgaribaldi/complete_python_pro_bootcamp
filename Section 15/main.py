### COFFEE MACHINE PROJECT ###

# The goal is to build the program for a coffee machine.

# Program Requirements
# Download the PDF for the program requirements here:
# https://drive.google.com/uc?export=download&id=1eIZt2TeFGVrk4nXkx8E_5Slw2coEcOUo

# Demo Project
# If you right-click on solution.py in the file navigator, you can "Run solution" without opening the file.
# You'll be able to test out the functionality in the output area and refer to the PDF to confirm all the functionality.

## Project Requirements
    # Print report
    # Check if resources are sufficient
    # Process coins
    # Check if transaction was successfull
    # Make the coffee
### COFFEE MACHINE PROJECT ###

from menu import MENU
from art import welcome
from properties import resources, coins

its_on = True
money = 0 

def report():
    """Imprime o relatório de recursos disponíveis na máquina."""
    print("• Current resources:")
    print(f"    - Water: {resources['water']}ml")
    print(f"    - Milk: {resources.get('milk', 0)}ml")
    print(f"    - Coffee: {resources['coffee']}g")
    print(f"    - Money: ${money:.2f}")

def check_resources(drink):
    """Verifica se há recursos suficientes para preparar a bebida escolhida."""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"• Sorry, there is not enough {item}.")
            return False
    return True

def process_payment(drink):
    """Calcula o pagamento do cliente e retorna True se o pagamento for bem-sucedido."""
    global money
    price = MENU[drink]["cost"]
    
    print(f"• The {drink} costs: ${price:.2f}. Please insert coins.")
    total_inserted = (
        int(input("How many quarters? ⇒ ")) * coins["quarters"] +
        int(input("How many dimes? ⇒ ")) * coins["dimes"] +
        int(input("How many nickles? ⇒ ")) * coins["nickles"] +
        int(input("How many pennies? ⇒ ")) * coins["pennies"]
    )
    
    if total_inserted < price:
        print(f"• Sorry, that's not enough money. Money refunded (${total_inserted:.2f}).")
        return False
    else:
        change = round(total_inserted - price, 2)
        money += price  # Adiciona ao caixa da máquina
        if change > 0:
            print(f"• Here is your change: ${change:.2f}")
        return True

def make_coffee(drink):
    """Deduz os recursos usados e entrega a bebida ao cliente."""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"• Here is your {drink}. Enjoy! ☕")

def coffee_machine():
    """Loop principal da máquina de café."""
    global its_on
    print(welcome)

    while its_on:
        command = input("\n• What would you like? (espresso/latte/cappuccino): \n⇒ ").lower()

        if command == "report":
            report()
        elif command == "off":
            print("• Turning off the coffee machine. See you soon!")
            its_on = False
        elif command in MENU:
            if check_resources(command):  
                if process_payment(command):  
                    make_coffee(command)  
        else:
            print("• Invalid command. Please choose espresso, latte, or cappuccino.")

coffee_machine()
