from models.armament import Armament


class Machinery(Armament):

    def __init__(self, weight: float, max_speed_mph: float):
        super().__init__(20000, "NA", 2000)
        self. weight = weight
        self.max_speed_mph = max_speed_mph
