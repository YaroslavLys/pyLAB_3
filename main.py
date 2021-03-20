from models.tank import Tank
from models.drone import Drone
from models.knife import Knife
from models.pistol import Pistol
from models.ghilliesuit import GhillieSuit
from manager.armament_manager import ArmamentManager
from manager.sort_order import SortOrder


def main():
    manager = ArmamentManager([Drone(), Tank(), Knife(), Pistol(), GhillieSuit()])
    print("========== Items for scouting ==========")
    manager.search_by("Scouting")
    manager.print_items()
    print("========== Sorted by price ==========")
    manager.sort_by_price(SortOrder.ASC)
    manager.print_items()
    print("========== Sorted by mortality rate ==========")
    manager.sort_by_mortality_rate(SortOrder.DESC)
    manager.print_items()


if __name__ == '__main__':
    main()
