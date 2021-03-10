from models import country


class Armament:

    def __init__(self, price: float, function: str, mortality_rate: int, origin_country: country = country):
        self.origin_country = origin_country
        self.price = price
        self.function = function
        self.mortality_rate = mortality_rate

    def __str__(self):
        return f"Item:\n  price: {self.price}\n  mortality rate: {self.mortality_rate}\n "
