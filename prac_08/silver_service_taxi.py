from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise silver service taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{}, plus flagfall of {}0".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get current fare"""
        return self.flagfall + super().get_fare()

