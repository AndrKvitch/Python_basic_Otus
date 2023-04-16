"""
создайте класс `Car`, наследник `Vehicle`
"""


from homework_02.engine import Engine
from homework_02.base import Vehicle

class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = Engine(volume=2.0, pistons=6)
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def set_engine(self, engine: Engine):
        if isinstance(engine, Engine):
            self.engine = engine

