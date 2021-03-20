import university
from armament import Armament


class Soldier:

    def __init__(self, name: str, age: int, alma_mater: university, experience: float, arsenal: Armament):
        self.name = name
        self.age = age
        self.alma_mater = alma_mater
        self.experience = experience
        self.arsenal = arsenal
