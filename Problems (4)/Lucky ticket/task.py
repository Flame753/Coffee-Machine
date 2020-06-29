# Save the input in this variable
ticket = str(input())

# Add up the digits for each half
half1 = sum([int(num) for num in ticket[0:3]])
half2 = sum([int(num) for num in ticket[3:6]])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")