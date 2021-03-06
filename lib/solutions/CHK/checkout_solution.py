import math

from collections import Counter
from itertools import combinations_with_replacement, permutations
from typing import List, Dict


class Offer:
    def __init__(self, name: str, base_items: Counter, free_items: Counter = Counter()):
        self.name = name
        self.base_items = base_items
        self.free_items = free_items

class Basket:
    def __init__(self, prices: Dict[str, int], items: Counter = Counter()):
        self.items = items
        self.prices = prices

    def add(self, sku: str) -> bool:
        """
        Add items to basket.
        """
        if sku not in self.prices:
            return False
        self.items[sku] += 1

    def update(self, skus: str) -> bool:
        """
        Replace basket items with a list.
        """
        self.items = Counter()
        for sku in skus:
            if sku not in self.prices:
                return False
            self.items[sku] += 1
        return True

    def contains(self, items: Counter) -> bool:
        """
        Check if all the given items exist in the basket.
        """
        res = (self.items & items) == items
        return res
    
    def remove(self, items: Counter) -> None:
        """
        Remove list of items from basket.
        """
        self.items -= items
        self.items += Counter() # cleanup
    
    def value(self) -> int:
        """
        Return value of basket.
        """
        return sum([self.prices[sku] * self.items[sku] for sku in self.items])

class OfferManager:
    def apply(basket: Basket, offers: List[Offer]) -> Basket:
        """
        Apply offers and return new basket.
        """
        best_value = math.inf
        best_basket = None

        # keep only applicable offers
        offers_applicable = []
        for offer in offers:
            if basket.contains(offer.base_items):
                offers_applicable.append(offer)

        if not offers_applicable:
            return basket

        # sort by offer size
        offers_applicable.sort(key=lambda x: len(x.base_items & basket.items), reverse=True)

        for offer in offers_applicable:
            while basket.contains(offer.base_items):  # check if offer can be applied
                basket.remove(offer.base_items)
                basket.remove(offer.free_items)
                basket.add(offer.name)
                # update best basket so far
                value = basket.value()
                if value < best_value:
                    best_value = value
                    best_basket = basket

        return best_basket

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    prices = {
        'A' : 50,
        'B' : 30,
        'C' : 20,
        'D' : 15,
        'E' : 40,
        'F' : 10,
        'G' : 20,
        'H' : 10,
        'I' : 35,
        'J' : 60,
        'K' : 80,
        'L' : 90,
        'M' : 15,
        'N' : 40,
        'O' : 10,
        'P' : 50,
        'Q' : 30,
        'R' : 50,
        'S' : 30,
        'T' : 20,
        'U' : 40,
        'V' : 50,
        'W' : 20,
        'X' : 90,
        'Y' : 10,
        'Z' : 50,
        '3A@130' : 130,
        '5A@200' : 200,
        '2B@45'  : 45,
        '5H@45' : 45,
        '10H@80': 80,
        '2K@150': 150,
        '5P@200' : 200,
        '3Q@80' : 80,
        '2V@90' : 90,
        '3V@130' : 130,
        '2E+1B' : 80,
        '2F+1F' : 20,
        '3N+1M' : 120,
        '3R+1Q' : 150,
        '3U+1U' : 120,
    }
    offers = [
        Offer('3A@130', base_items=Counter({'A': 3})),
        Offer('5A@200', base_items=Counter({'A': 5})),
        Offer('2B@45', base_items=Counter({'B': 2})),
        Offer('5H@45', base_items=Counter({'H': 5})),
        Offer('10H@80', base_items=Counter({'H': 10})),
        Offer('2K@150', base_items=Counter({'K': 2})),
        Offer('5P@200', base_items=Counter({'P': 5})),
        Offer('3Q@80', base_items=Counter({'Q': 3})),
        Offer('2V@90', base_items=Counter({'V': 2})),
        Offer('3V@130', base_items=Counter({'V': 3})),
        Offer('2E+1B', base_items=Counter({'E': 2}), free_items=Counter({'B': 1})),
        Offer('2F+1F', base_items=Counter({'F': 2}), free_items=Counter({'F': 1})),
        Offer('3N+1M', base_items=Counter({'N': 3}), free_items=Counter({'M': 1})),
        Offer('3R+1Q', base_items=Counter({'R': 3}), free_items=Counter({'Q': 1})),
        Offer('3U+1U', base_items=Counter({'U': 3}), free_items=Counter({'U': 1})),
    ]

    basket = Basket(prices)
    if not basket.update(skus):
        return -1

    basket = OfferManager.apply(basket, offers)

    return basket.value()




