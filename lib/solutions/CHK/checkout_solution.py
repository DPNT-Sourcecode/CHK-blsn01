from collections import Counter


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




