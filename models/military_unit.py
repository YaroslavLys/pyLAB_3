from personnel import Personnel
from models.armament import Armament


class MilitaryUnit:

    def __init__(self, year_formation: int, specialization: str, personnel_of_mu: Personnel, armament_of_mu: Armament):
        self.year_of_formation = year_formation
        self.specialization = specialization
        self.personnel_of_mu = personnel_of_mu
        self.armament_of_mu = armament_of_mu
