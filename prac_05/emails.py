"""
CP1404/ Practical
Email and names in a dictionary
"""


def main():
    """Dictionary of email to names"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(full_name))
        if confirmation.upper() != "Y" and confirmation != "":
            full_name = input("Name: ")
        email_to_name[email] = full_name
        email = input("Email:")
    # print list of name and email from dictionary
    for email, name in email_to_name.items():
        print(f"{name}, ({email})")


def get_name_from_email(email):
    """Try to get accurate name from the provided email"""
    f_name = email.split('@')[0]
    l_name = f_name.split('.')
    name = " ".join(l_name).title()
    return name


main()
