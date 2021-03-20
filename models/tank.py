from models.machinery import Machinery
from models.armament import Armament
from models.country import Country


class Tank(Machinery):

    def __init__(self, fuel_capacity: float = 20, type: str = "Heavy", ):
        Armament.__init__(self, 7000, "Defence", 1000, Country.CHINA)
        self.fuel_capacity = fuel_capacity
        self.type = type
