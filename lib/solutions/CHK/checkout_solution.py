from collections import Counter
from typing import List, Callable, Set


class Basket:
    def __init__(self, skus: Dict[str, int], offers: List[Callable]):
        self.counter = Counter()
        self.skus = skus
        self.offers = offers

    def put(sku: str) -> bool:
        if sku not in self.skus:
            return False
        self.counter += sku
        
        return True
    
    def value() -> int:
        pass

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    for sku in skus:

        counter[sku] += 1

        # check for 
        if counter['A'] == 3:
            counter['A'] -= 3
            counter['3A'] += 1
        
        if counter['B'] == 2:
            counter['B'] -= 2
            counter['2B'] += 1
