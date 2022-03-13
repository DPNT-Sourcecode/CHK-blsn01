from collections import Counter
from typing import List, Callable, Set


class Offer:
    def __init__(self, name: str, sku_set: Dict[str, int]):
        self.name = names
        self.sku_set = sku_set

class Basket:
    def __init__(self, sku_prices: Set[str], offers: List[Offer]):
        self.counter = Counter()
        self.sku_prices = sku_prices
        self.offers = offers

    def put(sku: str) -> bool:
        if sku not in self.sku_prices:
            return False

        self.counter[sku] += 1

        # check offers
        for offer in self.offers:
        
        return True
    
    def value() -> int:
        pass

"""
        if counter['A'] == 3:
            counter['A'] -= 3
            counter['3A'] += 1
        
        if counter['B'] == 2:
            counter['B'] -= 2
            counter['2B'] += 1
            """

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_prices = {
             'A' : 50,
             'B' : 30,
             'C' : 20,
             'D' : 15,
        '3A@130' : 130,
        '2B@45'  : 45
    }
    basket = Basket(sku_prices)

    for sku in skus:









