number_of_items = int(input("Enter number of items: "))
total_cost = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))

for i in range(number_of_items):
    cost = float(input("Enter item price: "))
    total_cost += cost

if total_cost > 100:
    total_cost = total_cost * .90
print(f"The total price for {number_of_items} items is ${total_cost:.2f}")
