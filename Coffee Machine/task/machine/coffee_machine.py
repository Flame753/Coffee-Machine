WATER = 200  # ml
MILK = 50  # ml
COFFEE_BEANS = 15  # g

message = "Write how many {} of {} the coffee machine has: "
# The amount of ingredient that are stocked
amount_water = int(input(message.format("ml", "water")))
amount_milk = int(input(message.format("ml", "milk")))
amount_beans = int(input(message.format("g", "coffee beans")))
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
