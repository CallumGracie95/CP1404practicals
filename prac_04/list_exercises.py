"List of integers and displaying output using functions and list index."

numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
first_number = numbers[0]
last_number = numbers[-1]
print(f"The first number is {first_number}")
print(f"The last number is {last_number}")
numbers.sort()
print(f"The smallest number is {numbers[0]}")
print(f"The largest number is {numbers[-1]}")
average = sum(numbers) / len(numbers)
print(f"The average of the numbers is {average}")
