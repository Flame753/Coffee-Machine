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
        print(f"{value[0]} of {key}")


def get_drink_inf(num, inf):
    """ inf: should be 'cost' or 'recipe' ONLY
        num: Should be between 1-3 """
    return drink_inf[drink_lis[num - 1]][inf]


def buy_drink():
    type_drink = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    recipe = get_drink_inf(type_drink, "recipe")
    cost = get_drink_inf(type_drink, "cost")
    for key, value in recipe.items():
        stock[key][0] = stock.get(key)[0] - value
    stock["disposable cups"][0] = stock["disposable cups"][0] - 1
    stock["money"][0] = int(stock["money"][0] + cost)  # Will need to remove int() to add decimals


def fill_supplies():
    message = "Write how many {} of {} do you want to add: "
    for item, value in stock.items():
        if value[1]:
            stock[item][0] = value[0] + int(input(message.format(value[1], item)))
        elif item == "disposable cups":
            stock[item][0] = value[0] + int(input(message.format(item, "coffee")))


def take_money():
    pass


show_supplies()
buy_drink()
show_supplies()
fill_supplies()
amount_ingredients = [amount_water // WATER, amount_beans // COFFEE_BEANS, amount_milk // MILK]
many_cups_made = min(amount_ingredients)
cups = int(input("Write how many cups of coffee you will need: "))
require_water = cups * WATER
require_milk = cups * MILK
require_beans = cups * COFFEE_BEANS

if amount_water >= require_water and amount_milk >= require_milk and amount_beans >= require_beans:
    enough = "Yes, I can make that amount of coffee"
    if many_cups_made > cups:
        print(enough + f"(and even {many_cups_made - cups} more than that)")
    else:
        print(enough)
else:
    print(f"No, I can make only {many_cups_made} cups of coffee")
