"""Taxi simulator program that used Taxi and SilverServiceTaxi classes"""
from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "(C)hoose taxi" \
       "(D)rive" \
       "(Q)uit"


def main():
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    choice = input("Choose: ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")
        elif choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("How far to drive? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        choice = input("Choose: ").upper()


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
