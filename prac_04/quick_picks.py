import random

NUMBER_OF_LINES = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks do you wish to generate? "))
    while number_of_quick_picks < 0:
        print("Enter a valid integer")
        number_of_quick_picks = int(input("How many quick picks do you wish to generate? "))

    # for number in range(number_of_quick_picks):
    #     quick_pick = random.randint(1, 45)
    #     print(quick_pick)
    #     print(quick_pick.sa)
    for i in range(number_of_quick_picks):
        random_integers = []
        for j in range(NUMBER_OF_LINES):
            random_line = random.randint(MINIMUM, MAXIMUM)
            random_integers.append(random_line)
        random_integers.sort()

        print(" ".join("{:2}".format(number) for number in random_integers))


main()
