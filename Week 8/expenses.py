def get_average_item_price(expenses: dict[str, list[float]]) -> float:
    """Return the average price of all the items in expenses. expenses is a 
    dictionary of people to lists of the prices of items each person purchased.
    """
    total = 0.0
    count = 0
    for person in expenses:
        for expense in expenses[person]:
            total = total + expense
            count = count + 1
    return total / count