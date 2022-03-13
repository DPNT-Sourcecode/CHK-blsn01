from collections import Counter
from typing import List, Callable


class Basket:
    def __init__(self, offers: List[Callable]):
        self.counter = Counter()
        self.offers = offers

    def put(sku: )

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    final_price = 0
    valid_skus = { 'A', 'B', 'C', 'D '}

    counter = Counter()

    for sku in skus:
        # check validity
        if sku not in valid_skus:
            return -1

        counter[sku] += 1

        # check for 
        if counter['A'] == 3:
            counter['A'] -= 3
            counter['3A'] += 1
        
        if counter['B'] == 2:
            counter['B'] -= 2
            counter['2B'] += 1






