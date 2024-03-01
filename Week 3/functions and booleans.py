def same_abs(num1: float, num2: float) -> bool:
    """Return True if and only if num1 and num2 have the same absolute value.

    >>> same_abs(-3.2, 3.2)
    True
    >>> same_abs(3.0, 3.5)
    False
    """
    return abs(num1) == abs(num2)

print("Testing same_abs: ")
if same_abs(-3.2, 3.2) == True and same_abs(3.0, 3.5) == False:
    print("same_abs passed\n")

def different_types(obj1: object, obj2: object) -> bool:
    """Return True if and only if obj1 and obj2 are of different types.

    >>> different_types(3, '3')
    True
    >>> different_types(108.0, 3.14)
    False
    """
    return type(obj1) != type(obj2)

print("Testing different_types: ")
if different_types(3, '3') == True and different_types(108.0, 3.14) == False:
    print("different_types passed\n")

# An extra exercise to try at home.
def is_right_triangle(side1: int, side2: int, hypotenuse: int) -> bool:
    """Return whether a triangle with sides of length side1, side2 and
    hypotenuse is a right triangle.

    >>> is_right_triangle(3, 4, 5)
    True
    >>> is_right_triangle(2, 2, 4)
    False
    """
    return side1 ** 2 + side2 ** 2 == hypotenuse ** 2

print("Testing is_right_triangle: ")
if is_right_triangle(3, 4, 5) == True and is_right_triangle(2, 2, 4) == False:
    print("is_right_triangle passed\n")