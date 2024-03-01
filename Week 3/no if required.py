def can_vote(age: int) -> bool:
    """Return True if and only if age is legal voting age of at least 18 years.

    >>> can_vote(16)
    False
    >>> can_vote(21)
    True
    """
    return age >= 18

print("Testing can_vote: ")
if can_vote(16) == False and can_vote(21) == True:
    print("can_vote passed\n")

TEEN_MIN = 13
TEEN_MAX = 18

def is_teenager(age: int) -> bool:
    """Return True if and only if age is a teenager between 13 and 18
    inclusive.

    >>> is_teenager(4)
    False
    >>> is_teenager(16)
    True
    >>> is_teenager(19)
    False
    """
    return TEEN_MIN <= age <= TEEN_MAX

print("Testing is_teenager: ")
if is_teenager(4) == False and is_teenager(16) == True and is_teenager(19) == False:
    print("is_teenager passed\n")