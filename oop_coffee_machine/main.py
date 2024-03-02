# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# def coffee_machine():
#     menu = Menu()
#     coffee_maker = CoffeeMaker()
#     money_machine = MoneyMachine()
#
#     should_continue = True
#
#     while should_continue:
#         order_name = input(f"What would you like? ({menu.get_items()}): ").lower()
#
#         if order_name == "off":
#             should_continue = False
#             print("Turning off the coffee machine.")
#         elif order_name == "report":
#             coffee_maker.report()
#             money_machine.report()
#         else:
#             drink = menu.find_drink(order_name)
#
#             if drink is not None:
#                 if coffee_maker.is_resource_sufficient(drink):
#                     if money_machine.make_payment(drink.cost):
#                         coffee_maker.make_coffee(drink)
#
# if __name__ == "__main__":
#     coffee_machine()
a = 3
if a == 3:
    print('CORRECT')