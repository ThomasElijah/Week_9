"""
CP1404/CP5632 Practical
Car class
"""


from Taxi import Car
import random

class UnreliableCar(Car):
    """Checks to see if car will start"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability


    def drive(self, distance):
        number = random.randint(0, 100)
        if number < self.reliability:
            super().drive(distance)
            return("Car started")
        else:
            return("Car failed to start")


def test():
    lemon = UnreliableCar("Lemon", 50, 45)
    print(lemon.drive(50))
    print(lemon.__str__())

test()