import personnel
import armament


class MilitaryUnit:

    def __init__(self, year_formation: int, specialization: str, personnel_of_mu: personnel, armament_of_mu: armament):
        self.year_of_formation = year_formation
        self.specialization = specialization
        self.personnel_of_mu = personnel_of_mu
        self.armament_of_mu = armament_of_mu
