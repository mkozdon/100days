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
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3,
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def show_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(resources, type):
    return [
        res
        for res in MENU[type]["ingredients"]
        if resources[res] < MENU[type]["ingredients"][res]
    ]


def process_payments(price):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    amount_paid = round(quarters + dimes + nickles + pennies, 2)
    print(amount_paid)
    print(price)
    if amount_paid == price:
        return True
    elif amount_paid > price:
        print(f"Here is ${amount_paid-price} dollars in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def take_resources(resources, type):
    for res in MENU[type]["ingredients"]:
        resources[res] -= MENU[type]["ingredients"][res]
    resources["money"] += MENU[type]["cost"]


def make_coffee(type):
    missing_resources = check_resources(resources, type)
    if len(missing_resources) == 0:
        if process_payments(MENU[type]["cost"]):
            take_resources(resources, type)
            print(f"Here is your {type}. Enjoy!")
    else:
        print(f"Sorry, there is not enough {', '.join(missing_resources)}.")


coffee_machine_running = True
while coffee_machine_running:
    user_selection = input("What would you like? (espresso/latte/capuccino): ")
    if user_selection == "off":
        coffee_machine_running = False
    elif user_selection == "report":
        show_report(resources)
    else:
        make_coffee(user_selection)
