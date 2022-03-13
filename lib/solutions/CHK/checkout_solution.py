from collections import Counter
from typing import List, Dict


class Offer:
    def __init__(self, name: str, items: Counter):
        self.name = name
        self.items = items

class Basket:
    def __init__(self, sku_prices: Dict[str, int], offers: List[Offer]):
        self.items = Counter()
        self.sku_prices = sku_prices
        self.offers = offers

    def put(self, sku: str) -> bool:
        if sku not in self.sku_prices:
            return False

        # Add to basket
        self.items[sku] += 1

        # Apply offers
        for offer in self.offers:
            if (self.items & offer.items) == offer.items:  # check if offer can be applied
                self.items -= offer.items
                self.items += Counter()  # clean up
                self.items[offer.name] += 1
        
        return True
    
    def value(self) -> int:
        return sum([self.sku_prices[sku] * self.items[sku] for sku in self.items])

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    sku_prices = {
             'A' : 50,
             'B' : 30,
             'C' : 20,
             'D' : 15,
        '3A@130' : 130,
        '2B@45'  : 45,
    }
    offers = [
        Offer('3A@130', Counter({ 'A' : 3 })),
        Offer('2B@45', Counter({ 'B' : 2 })),
    ]

    basket = Basket(sku_prices, offers)

    for sku in skus:
        if not basket.put(sku):
            return -1

    return basket.value()

