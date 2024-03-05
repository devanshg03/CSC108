def collect_underperformers(nums: list[int], threshold: int) -> list[int]:
    """Return a new list consisting of those numbers in nums that are below
    threshold, in the same order as in nums.
    
    >>> collect_underperformers([1, 2, 3, 4], 3)
    [1, 2]
    >>> collect_underperformers([1, 2, 108, 3, 4], 50)
    [1, 2, 3, 4]
    >>> collect_underperformers([], 7)
    []
    """
    
    result = []
    
    for item in nums:
        if item < threshold:
            result.append(item)
    
    return result


def keep_underperformers(nums: list[int], threshold: int) -> None:
    """Modify the existing list to only contain those numbers in nums that 
    are below threshold, in the same order as in nums.
    
    >>> nums = [4, 5, 6, 7]
    >>> keep_underperformers(nums, 7)
    >>> nums
    [4, 5, 6]
    """

    # We will be changing the length of a list so save it up front.
    length_list = len(nums)
    new_index = 0
    
    for i in range(length_list):
        
        # Remove all elements above or equal to threshold.
        # Update new index only if we don't remove anything.
        if nums[new_index] >= threshold:
            nums.remove(nums[new_index])
        else:
            new_index += 1
