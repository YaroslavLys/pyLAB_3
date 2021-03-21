from models import knifetype
from models.weapon import Weapon
from models.armament import Armament
from models.country import Country


class Knife(Weapon):

    def __init__(self, type: knifetype = knifetype, size: str = "Middle"):
        Armament.__init__(self, 100, "Scouting", 100, Country.GERMANY)
        self.type = type
        self.size = size
