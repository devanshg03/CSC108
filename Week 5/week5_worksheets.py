def collect_below_threshold(nums: list[int], threshold: int) -> list[int]:
    """Return a new list consisting of those numbers in nums that are below threshold,
    in the same order as in nums.
    >>> collect_below_threshold([1, 2, 3, 4], 3)
    [1, 2]
    >>> collect_below_threshold([1, 2, 108, 3, 4], 50)
    [1, 2, 3, 4]
    >>> collect_below_threshold([], 7)
    []
    """
    return [i for i in nums if isinstance(i, int) and i < threshold]

def scale_midterm_grades(grades: list[int], multiplier: int, bonus: int) -> None:
    """Modify each grade in grades by multiplying it by multiplier and then
    adding bonus. Cap grades at 100.
    >>> grades = [45, 50, 55, 95]
    >>> scale_midterm_grades(grades, 1, 10)
    >>> grades
    [55, 60, 65, 100]
    """
    for i in range(len(grades)):
        grades[i] = min((grades[i] * multiplier + bonus), 100)