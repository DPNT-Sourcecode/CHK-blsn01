from collections import Counter
from itertools import permutations
from typing import List, Dict


class Offer:
    def __init__(self, name: str, base_items: Counter, free_items: Counter = None):
        self.name = name
        self.base_items = base_items
        self.free_items = free_items

class Basket:
    def __init__(self, sku_prices: Dict[str, int]):
        self.items = Counter()
        self.sku_prices = sku_prices

    def add(self, sku: str) -> bool:
        """
        Add items to basket.
        """
        if sku not in self.sku_prices:
            return False
        self.items[sku] += 1

    def update(self, skus: str) -> bool:
        """
        Replace basket items.
        """
        self.items = Counter()
        for sku in skus:
            if sku not in self.sku_prices:
                return False
            self.items[sku] += 1
        return True
    
    def value(self) -> int:
        """
        Return value of basket.
        """
        return sum([self.sku_prices[sku] * self.items[sku] for sku in self.items])

class OfferManager:
    def apply(basket: Basket, offers: List[Offer]) -> Basket:
        """
        Apply offers and return new basket.
        """
        best_value = math.inf
        for offer_perm in permutations(offers):
            for offer in offer_perm:
                if (self.items & offer.base_items) == offer.base_items:  # check if offer can be applied
                    self.items -= offer.base_items
                    self.items += Counter()  # clean up
                    self.items[offer.name] += 1


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    sku_prices = {
        'A' : 50,
        'B' : 30,
        'C' : 20,
        'D' : 15,
        'E' : 40,
        '3A@130' : 130,
        '5A@200' : 200,
        '2B@45'  : 45,
        '2E+1B@45' : 80,
    }
    offers = [
        Offer('3A@130', base_items=Counter({'A': 3})),
        Offer('5A@200', base_items=Counter({'A': 5})),
        Offer('2B@45', base_items=Counter({'B': 2})),
        Offer('2E+1B@45', base_items=Counter({'E': 2}, free_items=Counter({'B': 1}))),
    ]

    basket = Basket(sku_prices)
    if not basket.update(skus):
        return -1

    basket = OfferManager.apply(basket, offers)

    return basket.value()







