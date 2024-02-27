def count_uppercase(s: str) -> int:
    """Return the number of uppercase letters in s.

    >>> count_uppercase('abc')
    0

    >>> count_uppercase('ABc')
    2
    """
    uppercase_count = 0
    for char in s:
        if char.isupper():
            uppercase_count += 1
    return uppercase_count


def all_fluffy(s: str) -> bool:
    """Return True if and only if every character in s is fluffy. Fluffy
    characters are those that appear in the word 'fluffy'.

    >>> all_fluffy('fluffy')
    True

    >>> all_fluffy('nice')
    False
    """
    for char in s:
        if char not in 'fluffy':
            return False
    return True


def add_underscores(s: str) -> str:
    """Return a string that contains the characters from s with an underscore
    added after every character except the last.

    >>> add_underscores('hello')
    'h_e_l_l_o' 

    >>> add_underscores('abc')
    'a_b_c'
    """
    result = ''
    for char in s[:-1]:
        result += char + '_'
    result += s[-1]
    return result
