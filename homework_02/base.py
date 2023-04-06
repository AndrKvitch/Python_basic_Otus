from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverLoad



class Vehicle(ABC):

    def __init__(self, weight=0, fuel=40, fuel_consumption=5):
        super().__init__()
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.start = False

    def weight(self):
        return self.weight

    def started(self):
        pass

    def start(self):
        if not self.started:
            if self.fuel < self.fuel_consumption:
                raise LowFuelError('Low fuel')
            else:
                self.started = True





    def move(self, distance):
        fuel_now = 6
        required_fuel = distance * (self.fuel_consumption)
        if fuel_now < required_fuel or fuel_now < self.fuel_consumption:
            raise NotEnoughFuel
        else:
            self.fuel -= required_fuel