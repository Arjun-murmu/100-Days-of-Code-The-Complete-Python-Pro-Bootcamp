from random import choice
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    # is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert a coin.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def make_coffe(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {item} ☕ Enjoy!")

def is_transaction_successfully(money_receive , drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_receive >= drink_cost:
        global profit
        change = round(money_receive - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

is_machine = True
while is_machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_machine = False

    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}ml")
        print(f"Money : ${profit}")

    else:
        drink = MENU[choice]
        # print(drink)
        # print(resources_sufficient(drink["ingredients"]))
        if resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successfully(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])



