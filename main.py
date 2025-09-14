
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
    "money": 0,
}
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

# TODO: 1. Print report of the coffee machine resources

def report(resources_dict):
    print(f"Water: {resources_dict['water']}ml")
    print(f"Milk: {resources_dict['milk']}ml")
    print(f"Coffee: {resources_dict['coffee']}g")
    print(f"Money: ${resources_dict['money']}")

# TODO 2. Create a function who checks if enough resources
def enough_resources(u_choice):
    for item in MENU[u_choice]['ingredients']:
        required_amount = MENU[u_choice]['ingredients'][item]
        available_amount = resources[item]


        if required_amount > available_amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coin_process():
    coin_sum= 0
    print("Please insert coins.")
    for item in coins:
        while True:
            try:
                coin =int(input(f"How many {item}?: ")) * coins[item]
                break
            except ValueError:
                print("Please enter a valid number")
        coin_sum += coin
    return coin_sum

def update_res(u_choice):
    for item in MENU[u_choice]['ingredients']:
        resources[item] -= MENU[u_choice]['ingredients'][item]
    resources['money'] += MENU[u_choice]['cost']
    if sum_coins > MENU[u_choice]['cost']:
        change = sum_coins - MENU[u_choice]['cost']
        print(f"Here is ${round(change,2)} in change")
    print(f"Here is your {u_choice} ☕ Enjoy!")







while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print("reporting...")
        report(resources)
        continue

    elif choice == "off":
        break
    try:
        print(f"Your {choice} costs ${MENU[choice]['cost']}")
    except KeyError:
        print("Sorry, you don't have this drink")
        continue

    if enough_resources(choice):
           sum_coins = coin_process()
           if sum_coins < MENU[choice]['cost']:
               print("Sorry that's not enough money. Money refunded.")
           else:

               update_res(choice)
