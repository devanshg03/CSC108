def stretch_string(s: str, stretch_factors: list[int]) -> str:
    """Return a string consisting of the characters in s in the same order as in s,
    repeated the number of times indicated by the item at the corresponding
    position of stretch_factors.

    Precondition: len(s) == len(stretch_factors) and the values in
                  stretch_factors are non-negative

    >>> stretch_string('Hello', [2, 0, 3, 1, 1])
    'HHllllo'
    >>> stretch_string('echo', [0, 0, 1, 5])
    hooooo
    """
    return ''.join([(s[i] * stretch_factors[i]) for i in range(len(s))])


def greatest_difference(nums1: list[int], nums2: list[int]) -> int:
    """Return the greatest absolute difference between numbers at corresponding
    positions in nums1 and nums2.

    Precondition: len(nums1) == len(nums2) and nums1 != []

    >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    >>> greatest_difference([1, -2, 3], [-6, 8, 10])
    10
    """
    return max([abs(nums1[i] - nums2[i]) for i in range(len(nums1))])