from collections import Counter
from typing import List, Callable, Set


class Offer:
    def __init__(self, name: str, items: Counter):
        self.name = name
        self.items = items

class Basket:
    def __init__(self, sku_prices: Set[str], offers: List[Offer]):
        self.items = Counter()
        self.sku_prices = sku_prices
        self.offers = offers

    def put(sku: str) -> bool:
        if sku not in self.sku_prices:
            return False

        # Add to basket
        self.items[sku] += 1

        # Apply offers
        for offer in self.offers:
            if self.items & offer.items
                self.items -= offer.items
                self.items += Counter()  # clean up
                self.items[offer.name] += 1
        
        return True
    
    def value() -> int:
        total = 0
        for item in self.items:
            total += 

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





