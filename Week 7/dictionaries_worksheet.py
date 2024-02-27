
# An order qualifies for express checkout if does not have more items than
# the EXPRESS_LIMIT
EXPRESS_LIMIT = 8

def express_checkout(product_to_quantity: dict[str, int]) -> bool:
    """Return True if and only if the grocery order in product_to_quantity
    qualifies for the express checkout. product_to_quantity maps products
    to the numbers of those items in the grocery order.
    
    >>> express_checkout({'banana': 3, 'soy milk': 1, 'peanut butter': 1})
    ???
    >>> express_checkout({'banana': 3, 'soy milk': 1, 'twinkie': 5})
    ???
    """


def build_placements(shoes: list[str]) -> dict[str, list[int]]:
    """Return a dictionary where each key is a company and each value is a
    list of placements by people wearing shoes made by that company.

    >>> result = build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', \
    'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics'])
    >>> result == {'Saucony': [1, 5, 9], 'Asics': [2, 3, 7, 10], 'NB': [4], \
    'Nike': [6], 'Adidas': [8]}
    True
    """
    

