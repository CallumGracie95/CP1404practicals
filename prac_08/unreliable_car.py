"""Activity that inherits car class"""

from random import randint
from prac_08.car import Car


class UnreliableCar(Car):
    """Special version of a Car that measures reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        rand_number = randint(0, 100)
        if rand_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

