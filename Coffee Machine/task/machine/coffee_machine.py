WATER = 200  # ml
MILK = 50  # ml
COFFEE_BEANS = 15  # g

message = "Write how many {} of {} the coffee machine has: "
water = int(input(message.format("ml", "water")))
milk = int(input(message.format("ml", "milk")))
coffee_beans = int(input(message.format("g", "coffee beans")))

cups = int(input("Write how many cups of coffee you will need: "))
print(f"For {cups} cups of coffee you will need:\n"
      f"{cups * WATER} ml of water\n"
      f"{cups * MILK} ml of milk\n"
      f"{cups * COFFEE_BEANS} g of coffee beans")
