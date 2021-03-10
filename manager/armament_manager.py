from manager.sort_order import SortOrder


class ArmamentManager:

    def __init__(self, items=list):
        self.items = items

    def search_by(self, function: str):
        out = list()
        for item in self.items:
            if item.function == function:
                out.append(item)
        self.items = out
        return out

    def sort_by_price(self, order: SortOrder):
        out = list()
        self.items.sort(key=lambda x: x.price, reverse=bool(order.value))
        out = self.items
        return out

    def sort_by_mortality_rate(self, order: SortOrder):
        out = list()
        self.items.sort(key=lambda x: x.mortality_rate, reverse=bool(order.value))
        out = self.items
        return out

    def print_items(self):
        for item in self.items:
            print(type(item))
            print(str(item))
