import unittest
from models.country import Country
from models.armament import Armament
from manager.armament_manager import ArmamentManager
from manager.sort_order import SortOrder
from models.drone import Drone
from models.tank import Tank
from models.knife import Knife
from models.pistol import Pistol
from models.ghilliesuit import GhillieSuit


class TestArmamentManager(unittest.TestCase):

    def setUp(self):
        self.drone = Drone()
        self.tank = Tank()
        self.knife = Knife()
        self.ghilliesuit = GhillieSuit()
        self.pistol = Pistol()
        arsenal = list()
        arsenal = [self.drone, self.tank, self.knife, self.pistol, self.ghilliesuit]
        self.manager = ArmamentManager(arsenal)

    def test_search_by(self):
        self.assertEqual(self.manager.search_by("Scouting"), [self.drone, self.knife, self.pistol, self.ghilliesuit])

    def test_sort_by_price(self):
        self.assertEqual(self.manager.sort_by_price(SortOrder.ASC),
                         [self.drone, self.knife, self.pistol, self.ghilliesuit, self.tank])

    def test_sort_by_mortality_rate(self):
        self.assertEqual(self.manager.sort_by_mortality_rate(SortOrder.DESC),
                         [self.tank, self.pistol, self.knife, self.drone, self.ghilliesuit])


class TestArmament(unittest.TestCase):

    def setUp(self):
        self.armament = Armament(20, "Attack", 300, Country.CHINA)

    def test_init(self):
        self.assertEqual(20, self.armament.price)
        self.assertEqual("Attack", self.armament.function)
        self.assertEqual(300, self.armament.mortality_rate)
        self.assertEqual(Country.CHINA, self.armament.origin_country)

    def test_str(self):
        self.assertEqual(str(self.armament),
                         f"Item:\n  price: {self.armament.price}\n  mortality rate: {self.armament.mortality_rate}\n ")


if __name__ == '__main__':
    unittest.main()
