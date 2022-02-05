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
            else:
                # valid = True
                return user_input


choice = user_choice()
choice = function_choice(choice)


print("Correct input")
print(choice)
