from collections import Counter
from typing import List, Callable, Set


class Basket:
    def __init__(self, valid_skus: Set[str], offers: List[Callable]):
        self.counter = Counter()
        self.valid_skus = valid_skus
        self.offers = offers

    def put(sku: str) -> bool:
        if sku not in self.valid_skus:
            return False
        self.counter += sku
        
        return True
    
    def 

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    final_price = 0
    valid_skus = { 'A', 'B', 'C', 'D '}

    counter = Counter()

    for sku in skus:

        counter[sku] += 1

        # check for 
        if counter['A'] == 3:
            counter['A'] -= 3
            counter['3A'] += 1
        
        if counter['B'] == 2:
            counter['B'] -= 2
            counter['2B'] += 1







