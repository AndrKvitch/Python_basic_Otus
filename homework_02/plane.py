"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverLoad


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__()
        self.cargo = 0
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, added_load):
        if self.cargo + added_load <= self.max_cargo:
            self.cargo += added_load
        else:
            raise CargoOverLoad

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result