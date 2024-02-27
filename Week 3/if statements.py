def earlier_name(name1: str, name2: str) -> str:
    """Return the name, name1 or name2, that comes first alphabetically.

    >>> earlier_name('Jen', 'Paul')
    'Jen'
    >>> earlier_name('Colin', 'Colin')
    'Colin'
    """
    if name1 < name2:
        return name1
    else:
        return name2
    
print("Testing earlier_name: ")
if earlier_name('Jen', 'Paul') == 'Jen' and earlier_name('Colin', 'Colin') == 'Colin':
        print("earlier_name passed\n")


def ticket_price(age: int) -> float:
    """Return the ticket price for a person who is age years old.
    Seniors 65 and over pay 4.75, kids 12 and under pay 4.25 and
    everyone else pays 7.50.

    Precondition: age > 0

    >>> ticket_price(7)
    4.25
    >>> ticket_price(21)
    7.5
    >>> ticket_price(101)
    4.75
    """
    if age <= 12:
        return 4.25
    elif age >= 65:
        return 4.75
    else:
        return 7.5
    
print("Testing ticket_price: ")
if ticket_price(7) == 4.25 and ticket_price(21) == 7.5 and ticket_price(101) == 4.75:
        print("ticket_price passed\n")


def format_name(first: str, last: str) -> str:
    """Return the first and last names as a single string, in the form:
    last, first
    Mononymous persons (those with no last name) should have their name
    returned without a comma.

    >>> format_name('Cherilyn', 'Sarkisian')
    'Sarkisian, Cherilyn'
    >>> format_name('Cher', '')
    'Cher'
    """
    if not last:
        return first
    else:
        return last + ', ' + first

print("Testing format_name: ")
if format_name('Cherilyn', 'Sarkisian') == 'Sarkisian, Cherilyn' and format_name('Cher', '') == 'Cher':
        print("format_name passed\n")