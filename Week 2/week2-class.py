def distance_to_origin(x: float, y:float) -> float:
    """Returns the distance from the origin to the point (x, y)
    
    >>> distance_to_origin(3.0, 4.0)
    5.0

    >>> distance_to_origin(-5.0, 12.0)
    13.0
    """
    return (x**2 + y**2)**0.5

def repeat_word(word: str, repeat_count: int) -> str:
    """Returns the string word repeated repeat_count times
    
    Precondition: repeat_count >= 0

    >>> repeat_word('Marcia ', 3)
    'Marcia Marcia Marcia '

    >>> repeat_word('Buffalo ', 8)
    'Buffalo Buffalo Buffalo Buffalo Buffalo Buffalo Buffalo Buffalo '
    """
    return word * repeat_count

def number_of_cents(change: float) -> int:
    """Returns the number of cents remaining from a total monetary amount after removing the whole dollar component from change.

    >>> number_of_cents(1.25)
    25

    >> number_of_cents(20.00)
    0
    """
    return round((change % 1) * 100)

def calculate_tax(bill: float, tax_rate: float) -> float:
    """ Returns the bill times the tax_rate to reflect the amount of tax to be paid on this bill.

    Precondition: 0.0 =< tax_rate =< 1.0

    >>> calculate_tax(50.0, 0.13)
    6.5

    >>> calculate_tax(62.0, 0.10)
    6.2
    """
    return bill * tax_rate

def format_name(first_name: str, last_name: str) -> str:
    """
    Returns a string in the format of last_name, first_name.
    
    >>> format_name('Devansh', 'Gandhi')
    'Gandhi, Devansh'

    >>> format_name('Jen', 'Campbell')
    'Campbell, Jen'
    """
    return last_name + ", " + first_name

def to_listing(first_name: str, last_name: str, phone_number: str) -> str:
    """
    Returns a string in the format of last_name, first_name: phone number.
    
    >>> to_listing('Devansh', 'Gandhi','555')
    'Gandhi, Devansh: 555'

    >>> to_listing('Jen', 'Campbell', '111')
    'Campbell, Jen: 111'
    """
    return format_name(first_name, last_name) + ": " + phone_number

def report_size(n: int) -> str:
    """Return 'small' if n is between 0 and 20 inclusive,
    'medium' if n is between 21 and 40 inclusive,
    and 'large' if n is 41 or greater.
    
    Precondition: n >= 0
    
    >>> report_size(4)
    'small'
    >>> report_size(24)
    'medium'
    >>> report_size(45)
    'large'
    """
def extract(s: str, start: int, stop: int) -> str:
    """Return the substring of s from index start (inclusive) to index stop (exclusive).

    Precondition: 0 <= start <= stop <= len(s)
        
    >>> extract('birthday', 1, 4)
    'irt' 
    >>> extract('toronto', 2, 5)
    'ron'     
    """
    return s[start:stop]

def swap_ends(message: str) -> str:
    """Return a new string that is message with the first and last
    characters swapped.
    
    Precondition: len(message) >= 2
    
    >>> swap_ends('cat')
    'tac'
    >>> swap_ends('breakfast for dinner!')
    '!reakfast for dinnerb'
    """
    last_char = message[len(message) - 1]
    middle = message[1:len(message) - 1]
    first_char = message[0]
    return last_char + middle + first_char