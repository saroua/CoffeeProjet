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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def user_choice():
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return question


choice = user_choice()
# print(user_choice)

while choice not in ["off", "cappuccino", "latte", "report", "espresso"]:
    print("Invalid input, please enter valid input.")
    choice = user_choice()

if choice == "off":
    print("Coffee machine turning off, goodbye.")
    exit()

elif choice == "report":
    print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}
""")
    while choice not in ["off", "cappuccino", "latte", "espresso"]:
        choice = user_choice()
        if choice == "off":
            print("Coffee machine turning off, goodbye.")
            exit()
        if choice not in ["cappuccino", "latte", "espresso"]:
            print("Invalid input, please enter valid input.")

print("Correct input")