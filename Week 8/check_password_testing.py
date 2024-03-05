def check_password(passwd: str) -> bool:
    """A strong password has a length greater than or equal to 6, contains at
    least one lowercase letter, at least one uppercase letter, and at least
    one digit.  Return True if and only if passwd is considered strong.

    >>> check_password('I<3csc108')
    True
    >>> check_password('Hell00')
    True
    >>> check_password('Helll0')
    True
    >>> check_password('Hell000')
    True
    >>> check_password('hell000')
    False
    >>> check_password('H123456')
    False
    >>> check_password('Abcdef')
    False
    >>> check_password('')
    False
    >>> check_password('Ab0')
    False
    """
    has_upper = False
    has_lower = False
    has_digit = False

    for ch in passwd:

        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
            
    return len(passwd) >= 6 and has_upper and has_lower and has_digit

if __name__ == '__main__':
    import doctest
    doctest.testmod()