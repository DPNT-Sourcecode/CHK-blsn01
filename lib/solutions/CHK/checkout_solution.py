from collections import Counter
from typing import List, Callable, Set


class Offer:
    def __init__(self, name: str, sku_set: Counter):
        self.name = name
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
            tmp_counter = self.counter & offer.sku_set
        
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
def checkout(skus) -> int:
    sku_prices = {
             'A' : 50,
             'B' : 30,
             'C' : 20,
             'D' : 15,
        '3A@130' : 130,
        '2B@45'  : 45,
    }
    offers = [
        Offer('3A@130', { 'A' : 3 }),
        Offer('2A@45', { 'B' : 2 }),
    ]

    basket = Basket(sku_prices, offers)

    for sku in skus:
        if not basket.put(sku):
            return -1

    return basket.value()



