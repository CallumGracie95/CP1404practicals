"""Guitar class activity"""
CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, ({self.year}), ${self.cost:.2f}"

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE


def main():
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_added = Guitar(name, year, cost)
        print(f"{guitar_added} added")
        guitars.append(guitar_added)
        name = input("Guitar name: ")

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(
                "Guitar {0}: {1.name:>13} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
