# The types of drinks that the coffee shop has.
drink_lis = ["espresso", "latte", "cappuccino"]
drink_inf = {"espresso": {"cost": 4.0,
                          "recipe": {"water": 250,
                                     "coffee beans": 16}},
             "latte": {"cost": 7.0,
                       "recipe": {"water": 350,
                                  "milk": 75,
                                  "coffee beans": 20}},
             "cappuccino": {"cost": 6.0,
                            "recipe": {"water": 200,
                                       "milk": 100,
                                       "coffee beans": 12}}
             }
# What the store has in stock.
stock = {"water": [400, "ml"],
         "milk": [540, "ml"],
         "coffee beans": [120, "grams"],
         "disposable cups": [9, None],
         "money": [550, None]}


def show_supplies():
    print("The coffee machine has: ")
    for key, value in stock.items():
        if key == "money":
            print(f"${value[0]} of {key}")
        else:
            print(f"{value[0]} of {key}")


def get_drink_inf(drink_num, inf):
    """ inf: should be 'cost' or 'recipe' ONLY
        num: Should be between 1-3 """
    return drink_inf[drink_lis[drink_num - 1]][inf]


def have_enough(drink_num):
    """ Returns: True if have enough items and False if not"""
    recipe = get_drink_inf(drink_num, "recipe")
    ans = list()
    for key, value in recipe.items():
        if stock[key][0] >= value and stock["disposable cups"] != 0:
            ans.append(True)
        else:
            ans.append(False)
    return all(ans)


def what_not_enough(drink_num):
    """ Returns: A list of items don't have enough of """
    recipe = get_drink_inf(drink_num, "recipe")
    ans = list()
    for key, value in recipe.items():
        if stock[key][0] < value:
            ans.append(key)
        elif stock["disposable cups"] == 0:
            ans.append("disposable cups")
    return ans


def buy_drink():
    type_drink = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    recipe = get_drink_inf(type_drink, "recipe")
    cost = get_drink_inf(type_drink, "cost")
    if have_enough(type_drink):
        for name_item, value in recipe.items():
            stock[name_item][0] = stock.get(name_item)[0] - value
        stock["disposable cups"][0] = stock["disposable cups"][0] - 1
        stock["money"][0] = int(stock["money"][0] + cost)  # Remove int() to add decimals to make it more realistic
        print("I have enough resources, making you a coffee!")
    else:
        print(f"Sorry, not enough {what_not_enough(type_drink)}!")


def fill_supplies():
    message = "Write how many {} of {} do you want to add: "
    for item, value in stock.items():
        if value[1]:
            stock[item][0] = value[0] + int(input(message.format(value[1], item)))
        elif item == "disposable cups":
            stock[item][0] = value[0] + int(input(message.format(item, "coffee")))


def take_money():
    print(f"I gave you ${stock['money'][0]}")
    stock["money"][0] = 0


while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    print()
    if action == "buy":
        buy_drink()
        print()
    elif action == "fill":
        fill_supplies()
        print()
    elif action == "take":
        take_money()
        print()
    elif action == "remaining":
        show_supplies()
        print()
    elif action == "exit":
        break
