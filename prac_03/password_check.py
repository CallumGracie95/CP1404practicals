"""Password checking program"""
MIN_LENGTH = 6


def main():
    password = get_password()
    display_asterisk_password(password)


def get_password():
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must have at least {MIN_LENGTH} characters.")
        password = input("Enter password: ")
    return password


def display_asterisk_password(password):
    for char in password:
        print("*", end="")


main()
