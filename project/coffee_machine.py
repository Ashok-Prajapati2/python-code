# Define the available drinks in the MENU dictionary, including their ingredients and cost.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 50,
            "coffee": 8
        },
        'cost': 15
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 25
        },
        'cost': 25
    },
    "cappuccino": {
        "ingredients": {
            "water": 300,
            "milk": 200,
            "coffee": 24
        },
        'cost': 35
    },
}

# Initialize the profit variable as a float (0.0).
profit = 0.0

# Initialize the resources available for making coffee.
resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}

# Define a function to check if there are sufficient resources for a given drink.
def is_resouress_sufficient(drink):
    drink = drink['ingredients']
    for item in drink:
        if resources[item] < drink[item]:
            print(f"{item} is not sufficient")
            return False
    return True

# Define a function to check if the payment is sufficient and calculate change.
def payment_succeful(payment):
    if payment >= drink['cost']:
        print(f"Your change: ${payment - drink['cost']}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

# Define a function to make the selected coffee, deducting resources, and returning the cost of the drink.
def make_coffee(drink):
    for item in drink['ingredients']:
        resources[item] = resources[item] - drink['ingredients'][item]
    print(f"Here is your {choice}. Enjoy!")
    return drink['cost']

# Initialize a loop to run the coffee machine program.
is_it = True

while is_it:
    choice = input("What would you like (espresso, latte, cappuccino): ")

    if choice == "off":
        is_it = False
    elif choice == "report":
        # Display the current resource quantities and profit.
        print(resources)
        print(f"Profit is ${profit:.2f}")
    else:
        # Get the selected drink from the MENU.
        drink = MENU[choice]

        if is_resouress_sufficient(drink):
            payment = int(input("Make payment: "))
            
            if payment_succeful(payment):
                # Update the profit and deduct resources when a successful payment is made.
                profit += make_coffee(drink)
