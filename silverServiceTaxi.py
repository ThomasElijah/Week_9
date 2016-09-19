from Taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagFall = 4.50

    def __init__(self, name , fuel, fanciness):
        super().__init__(name,fuel)
        self.fanciness = fanciness

    def get_fare(self):
        return(self.current_fare_distance * (Taxi.price_per_km * self.fanciness) + SilverServiceTaxi.flagFall)


def test():
    ssvTest = SilverServiceTaxi("ssvTest", 200, 2)
    ssvTest.drive(10)
    print("The cost of this trip is{:.2f}".format(ssvTest.get_fare()))
test()