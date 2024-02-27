CHILD = 'child'
ADULT = 'adult'
SENIOR = 'senior'

def overdue_fees(days_late: int, age_group: str) -> float:
    """Return the fees for a book that is days_late days late for a borrower
    in the age group age_group.
    
    Preconditions:
        - days_late >= 0
        - age_group is one of CHILD, ADULT or SENIOR

    >>> overdue_fees(2, SENIOR) # 2 days late, SENIOR borrower
    0.5
    >>> overdue_fees(5, ADULT) # 5 days late, ADULT borrower
    10.0
    """
    if days_late < 4:
        fees = days_late * 1
    elif days_late <= 6:
        fees = days_late * 2
    else:
        fees = days_late * 3
    
    if age_group == SENIOR:
        return fees / 4.0
    elif age_group == CHILD:
        return fees / 2.0
    else:
        return fees
    
def count_non_digits(s: str) -> int:
    """Return the number of non-digits in s.

    >>> count_non_digits('abc12d')
    4
    >>> count_non_digits('135')
    0
    >>> count_non_digits('A.4')
    2
    """
    non_digit_count = 0
    
    for char in s:
        if not char.isdigit():
            non_digit_count += 1
    return non_digit_count

def contains_no_lowercase_vowels(phrase: str) -> bool:
    """Return True if and only if phrase does not contain any lowercase
    vowels.

    >>> contains_no_lowercase_vowels('syzygy')
    True
    >>> contains_no_lowercase_vowels('e')
    False
    >>> contains_no_lowercase_vowels('abc')
    False
    """
    for char in phrase:
        if char in ('a', 'e', 'i', 'o', 'u'):
            return False
    return True

def more_upper_than_lower(message: str) -> bool:
    """Return True if and only if message contains more uppercase letters than
    lowercase letters.

    >>> more_upper_than_lower('I LOVE Caps Lock! :D')
    True
    >>> more_upper_than_lower('Does THIS Work?')
    False
    """ 
    upper_count = 0
    lower_count = 0

    for char in message:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count > lower_count