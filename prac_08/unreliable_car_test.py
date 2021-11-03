from prac_08.unreliable_car import UnreliableCar


def main():
    """Test unreliable cars"""
    new_car = UnreliableCar("Toyota Corolla", 100, 95)
    old_car = UnreliableCar("Nissan Pathfinder", 100, 40)

    for i in range(1, 10):
        print("Attempting to drive {}km".format(i))
        print("{:12} drove {:2}km".format(new_car.name, new_car.drive(i)))
        print("{:12} drove {:2}km".format(old_car.name, old_car.drive(i)))

    print(new_car)
    print(old_car)


main()
