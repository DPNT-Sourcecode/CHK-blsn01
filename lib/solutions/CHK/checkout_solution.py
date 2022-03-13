from collections import Counter
from typing import List, Callable, Set


class Offer:
    def __init__(self, name: str, sku_set: Dict[str, int], price: int):
        self.name = names
        self.sku_set = sku_set

class Basket:
    def __init__(self, valid_skus: Set[str], prices: Dict[str, int], offers: List[Offer]):
        self.counter = Counter()
        self.valid_skus = valid_skus
        self.prices = prices
        self.offers = offers

    def put(sku: str) -> bool:
        if sku not in self.valid_skus:
            return False
        self.counter[sku] += 1
        
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

    valid_skus = {'A', 'B', 'C', 'D', '3A@130'}
    basket = Basket()

    for sku in skus:







