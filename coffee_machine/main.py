from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
money = MoneyMachine()
is_game_on = True


while is_game_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:")
    if choice == "report":
        coffeeMaker.report()
        money.report()
    elif choice == "off":
        is_game_on = False
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
