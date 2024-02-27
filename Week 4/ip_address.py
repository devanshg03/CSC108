# Class Example
def is_IP_address(address: str) -> bool:
    """Returns True iff address contains only digits and periods.

    >>> is_IP_address('255.14.128.1')
    True
    >>> is_IP_address('40 St. George St.')
    False
    """
    for ch in address:
        if ch not in '0123456789.':
            return False
    return True

# Advanced Version
def is_ip_address(address: str) -> bool:
    """Returns True iff address is a valid IPv4 address.

    >>> is_IP_address('255.14.128.1')
    True
    >>> is_IP_address('40 St. George St.')
    False
    """
    for ch in address:
        if ch not in '0123456789.':
            return False
        address_list = address.split('.')
        if len(address_list) != 4:
            return False
        for octet in address_list:
            if not (0 <= int(octet) <= 255):
                return False
    return True