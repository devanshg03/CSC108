import unittest

def is_teenager(age: int) -> bool:
    """
    Return True if and only if age is a teenager between 13 and 18 inclusive.
    Precondition: age >= 0

    >>> is_teenager(0)
    False
    >>> is_teenager(5)
    False
    >>> is_teenager(13)
    True
    >>> is_teenager(16)
    True
    >>> is_teenager(18)
    True
    >>> is_teenager(25)
    False
    >>> is_teenager(113)
    False
    """
    return age > 13 and age <= 18
        
class TestIsTeenager(unittest.TestCase):
    def test_is_teenager(self):
        self.assertFalse(is_teenager(0))
        self.assertFalse(is_teenager(5))
        self.assertTrue(is_teenager(13))
        self.assertTrue(is_teenager(16))
        self.assertTrue(is_teenager(18))
        self.assertFalse(is_teenager(25))
        self.assertFalse(is_teenager(113))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)