from models.armament import Armament
from models import camouflagetype, cloth
from models.country import Country


class GhillieSuit(Armament):

    def __init__(self, type: camouflagetype = camouflagetype, size: str = "XXL", cloth: cloth = cloth):
        Armament.__init__(self, 300, "Scouting", 0, Country.UNITED_STATES)
        self.type = type
        self.size = size
        self.cloth = cloth
