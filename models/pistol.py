from models.weapon import Weapon
from models.armament import Armament


class Pistol(Weapon):

    def __init__(self, caliber: str = "7.62mm", name: str = "Glock"):
        Armament.__init__(self, 200, "Scouting", 500)
        self.caliber = caliber
        self.name = name
