WATER = 200  # ml
MILK = 50  # ml
COFFEE_BEANS = 15  # g

cups = int(input("Write how many cups of coffee you will need: "))
print(f"For {cups} cups of coffee you will need:\n"
      f"{cups * WATER} ml of water\n"
      f"{cups * MILK} ml of milk\n"
      f"{cups * COFFEE_BEANS} g of coffee beans")
