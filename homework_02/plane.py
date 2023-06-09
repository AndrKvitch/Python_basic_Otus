"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__()
        self.cargo = 0
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, added_load: int):
        if self.cargo + added_load <= self.max_cargo:
            self.cargo += added_load
        else:
            raise CargoOverload("Cargo over")

    def remove_all_cargo(self) -> int:
        result = self.cargo
        self.cargo = 0
        return result