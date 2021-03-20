from models.machinery import Machinery
from models.armament import Armament
from models.country import Country


class Drone(Machinery):

    def __init__(self, range: float = 20, model: str = "MODEL S"):
        Armament.__init__(self, 20, "Scouting", 50, Country.UKRAINE)
        self.range = range
        self.model = model
