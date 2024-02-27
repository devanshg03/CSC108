def digital_sum(nums_list: list[str]) -> int:
    """Return the sum of all the digits in all strings in nums_list.

    Precondition: s.isdigit() holds for each string s in nums_list.

    >>> digital_sum(['64', '128', '256'])
    34
    >>> digital_sum(['12', '3'])
    6
    """
    sum = 0
    for num in nums_list:
        for char in num:
            sum += int(char)
    return sum



def can_pay_with_two_coins(denoms: list[int], amount: int) -> bool:
    """Return True if and only if it is possible to form amount, which is a
    number of cents, using exactly two coins, which can be of any of the
    denominatins in denoms.

    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 20)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    False
    """
    for i in range (len(denoms)):
        for j in range (i, len(denoms)):
            if denoms[i] + denoms[j] == amount:
                return True
    return False
