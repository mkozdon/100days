from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


coffee_machine_running = True
while coffee_machine_running:
    user_selection = input("What would you like? (espresso/latte/capuccino): ")
    if user_selection == "off":
        coffee_machine_running = False
    elif user_selection == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        selected_item = menu.find_drink(user_selection)
        if coffee_machine.is_resource_sufficient(selected_item):
            if money_machine.make_payment():
                coffee_machine.make_coffee(selected_item)
