def every_nth_character(s: str, n: int) -> str:
    """Return a string containing every nth character from s, starting at index 0.

    Precondition: n > 0

    >>> every_nth_character('Computer Science', 3)
    'CpeSee'
    """

    result = ''
    i = 0  # The index of the next character to examine.

    while i < len(s):
        result += s[i]
        i += n

    return result


def find_letter_n_times(s: str, letter: str, n: int) -> str:
    """Return the smallest substring of s starting from index 0 that contains
    n occurrences of letter.

    Precondition: letter occurs at least n times in s

    >>> find_letter_n_times('Computer Science', 'e', 2)
    'Computer Scie'
    """

    i = 0  # The index of the next character to examine.
    count = 0  # The number of occurrences of letter in s[:i].

    while i < len(s) and count < n:
        if s[i] == letter:
            count = count + 1
        i = i + 1

    return s[:i]


def count_collatz_steps(n: int) -> int:
    """Return the number of steps it takes to reach 1 by applying the two rules
    of the Collatz conjecture beginning from the positive integer n.

    Precondition: n >= 1

    >>> count_collatz_steps(6)
    8
    """
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps += 1
    return steps


def first_digit(s: str) -> int:
    """Finds the first digit in the string and returns the index of the first digit.
    
    Precondition: s must contain at least one digit

    >>> first_digit('a1')
    1

    >>> first_digit('nice 1')
    5
    """

    i = 0

    while i < len(s) and s[i] not in '0123456789':
        i = i + 1
    return i
