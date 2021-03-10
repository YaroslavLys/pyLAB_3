from models.armament import Armament


class Weapon(Armament):

    def __init__(self, weight: float, reliability: str):
        Armament.__init__(self, 1000, "Scouting", 100)
        self.weight = weight
        self.reliability = reliability
