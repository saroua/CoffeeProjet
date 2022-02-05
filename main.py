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

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def user_choice():
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while question not in ["off", "cappuccino", "latte", "report", "espresso"]:
        print("Invalid input, please enter valid input.")
        question = user_choice()
    return question


def function_choice(user_input):
    valid = False
    while not valid:
        if user_input == "off":
            print("Coffee machine turning off, goodbye.")
            exit()
        elif user_input == "report":
            print(f"""    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${resources["money"]}
        """)
            while user_input not in ["off", "cappuccino", "latte", "espresso"]:
                user_input = user_choice()
                if user_input == "off":
                    print("Coffee machine turning off, goodbye.")
                    exit()
                if user_input not in ["cappuccino", "latte", "espresso"]:
                    print("Invalid input, please enter valid input.")
        elif user_input == "espresso":
            if resources["water"] < 50:
                print("Please refill water")
                exit()
            elif resources["coffee"] < 18:
                print("Please refill coffee")
                exit()
            else:
                # valid = True
                return user_input
        elif user_input == "latte":
            if resources["water"] < 200:
                print("Please refill water")
                exit()
            elif resources["coffee"] < 24:
                print("Please refill coffee")
                exit()
            elif resources["milk"] < 150:
                print("Please refill milk")
                exit()
            else:
                # valid = True
                return user_input
        else:
            if resources["water"] < 250:
                print("Please refill water")
                exit()
            elif resources["coffee"] < 24:
                print("Please refill coffee")
                exit()
            elif resources["milk"] < 100:
                print("Please refill milk")
                exit()
            else:
                # valid = True
                return user_input


def paying(user_input):
    user_choice_cost = MENU[user_input]["cost"]
    print(f"Your {user_input} will be {user_choice_cost}$")
    print("Please insert coins.")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))

    user_total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    choice_total = user_choice_cost

    change = round(user_total - choice_total, 2)

    if user_total < choice_total:
        print("Not enough money.")
        exit()
    else:
        print(f"Here is {change}$ in change")
        print(f"Here is yours {user_input}☕ . Enjoy")

    actual_coffee = resources["coffee"]
    actual_water = resources["water"]
    actual_milk = resources["milk"]
    actual_money = resources["money"]

    resources["coffee"] = actual_coffee - MENU[user_input]["ingredients"]["coffee"]
    resources["water"] = actual_water - MENU[user_input]["ingredients"]["water"]
    if user_input not in ["espresso"]:
        resources["milk"] = actual_milk - MENU[user_input]["ingredients"]["milk"]
    resources["money"] = actual_money + MENU[user_input]["cost"]


while True:
    choice = user_choice()
    choice = function_choice(choice)
    paying(choice)

#print("Correct input")
#print(choice)
