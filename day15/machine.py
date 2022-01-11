from main import MENU, resources


# function that check the amount of resources the machine has
def report(water, coffee, milk, money):
    """Reporting the amount of resources and money of the machine"""
    print(f"Water: {water}ml")
    print(f"Coffee: {coffee}g")
    print(f"Milk: {milk}ml")
    print(f"Money: ${money}")


# function to check the user's choice and execute
def items_value(ingredient, drink_ingredients):
    """ Checking if the drink's resource exist in the list"""
    if ingredient in drink_ingredients:
        return drink_ingredients[ingredient]
    else:
        return 0


# function that will verify if the machine has enough resources to make the user's drink
def enough_resource(water, coffee, milk, total_water, total_coffee, total_milk):
    """Verify if the machine has enough resources to make the user's drink"""
    if water > total_water:
        print("Sorry there is not enough water")
        return False
    elif coffee > total_coffee:
        print("Sorry there is not enough coffee")
        return False
    elif milk > total_milk:
        print("Sorry there is not enough milk")
        return False
    else:
        return True


def cost_calc(drink_cost, quarters, dimes, nickles, pennies):
    """Calculating the client change"""
    total_paid = quarters + dimes + nickles + pennies
    total_charge = round(total_paid - drink_cost, 4)
    if total_paid >= drink_cost:
        print(f"Here is ${total_charge} change.")
    else:
        print("there is not enough money")


def machine():
    """"""
    total_water = resources['water']
    total_coffee = resources['coffee']
    total_milk = resources['milk']
    total_money = 0
    ingredients = ['water', 'milk', 'coffee']
    water_value = 0
    milk_value = 0
    coffee_value = 0
    machine_on = True
    while machine_on:
        user_answer = input("What would you like? (espresso/latte/cappuccino):")
        if user_answer == 'report':
            report(total_water, total_coffee, total_milk, total_money)
        elif user_answer == 'off':
            machine_on = False
        elif user_answer == 'espresso' or 'latte' or 'cappuccino':
            dic_ingredients = MENU[user_answer]
            dic_ingredients = dic_ingredients["ingredients"]
            dic_cost = MENU[user_answer]
            dic_cost = dic_cost["cost"]
            for i in ingredients:
                a = items_value(i, dic_ingredients)
                if i == 'water':
                    water_value = a
                elif i == 'milk':
                    milk_value = a
                elif i == 'coffee':
                    coffee_value = a
            if enough_resource(water_value, coffee_value, milk_value, total_water, total_coffee, total_milk):
                total_water -= water_value
                total_coffee -= coffee_value
                total_milk -= milk_value
                total_money += dic_cost
                print("Please insert coins.")
                quarters = int(input("how many quarters?: ")) * 0.25
                dimes = int(input("how many dimes?: ")) * 0.1
                nickles = int(input("how many nickles?: ")) * 0.05
                pennies = int(input("how many pennies?: ")) * 0.01
                cost_calc(drink_cost=dic_cost, quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)
                print(f"Here is your {user_answer}. Enjoy")
            else:
                continue


machine()

