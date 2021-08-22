"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = get_valid_number()
    display_score(score)
    random_result = get_random_result()
    print(random_result)
    display_score(random_result)


def get_random_result():
    random_number = random.randint(0, 100)
    return random_number


def display_score(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score < 50:
        print("Bad")


def get_valid_number():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


main()
