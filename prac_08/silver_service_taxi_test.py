"""Silver service taxi test program"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi = SilverServiceTaxi("Gucci Taxi", 100, 2)
    silver_taxi.drive(18)
    print(silver_taxi)
    print("${}0".format(silver_taxi.get_fare()))


main()
