"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    pass


class NotEnoughFuel(Exception):
    pass

class CargoOverLoad(Exception):
    def __init__(self, exeption_cargo_over):
        self.exeption_cargo_over = exeption_cargo_over

    @property
    def exeption(self):
        return self.exeption_cargo_over

c = CargoOverLoad('Cargo error')
