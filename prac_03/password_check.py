MIN_LENGTH = 6
password = input("Enter password: ")
while len(password) < MIN_LENGTH:
    print(f"Password must have at least {MIN_LENGTH} characters.")
    password = input("Enter password: ")
for char in password:
    print("*", end="")
