def bubble_sort(L: list) -> None:
    """Sorts the items of L from smallest to largest using the 
    bubble sort algorithm.

    >>> unsorted = [3, 5, 2, 1, 4]
    >>> bubble_sort(unsorted)
    >>> unsorted
    [1, 2, 3, 4, 5]

    >>> unsorted = [5, 3, 8, 6, 2, 1]
    >>> bubble_sort(unsorted)
    >>> unsorted
    [1, 2, 3, 5, 6, 8]
    """
    # The index of the last unsorted item
    end = len(L) - 1

    while end != 0:
        for i in range(end):
            if L[i] > L[i + 1]:
                # Swap the items
                L[i], L[i + 1] = L[i + 1], L[i]
        end = end - 1

def get_index_of_min(L: list, i: int) -> int:
    """Returns the index of the smallest item in L[i:].

    >>> get_index_of_min([2, 7, 3, 5], 1)
    2
    """
    index_of_min = i

    for j in range(i + 1, len(L)):
        if L[j] < L[index_of_min]:
            index_of_min = j

    return index_of_min

def selection_sort(L: list) -> None:
    """ Sorts the items of L from smallest to largest using the
    selection sort algorithm.
    
    >>> unsorted = [3, 5, 2, 1, 4]
    >>> selection_sort(unsorted)
    >>> unsorted
    [1, 2, 3, 4, 5]

    >>> unsorted = [5, 3, 8, 6, 2, 1]
    >>> selection_sort(unsorted)
    >>> unsorted
    [1, 2, 3, 5, 6, 8]
    """
    for i in range(len(L)):
        # Find the index of the smallest item in L[i:]
        index_of_min = get_index_of_min(L, i)
        L[i], L[index_of_min] = L[index_of_min], L[i]

def insert(L: list, i: int) -> None:
    """Precondition: L[:i] is sorted from smallest to largest.

    Move L[i] to where it belongs in L[:i + 1].

    >>> L = [7, 3, 5, 2]
    >>> insert(L, 1)
    >>> L
    [3, 7, 5, 2]
    """
    # The value to be inserted into the sorted part of the list.
    value = L[i]
    # Find the index, j, where the value belongs.
    j = i
    while j != 0 and L[j - 1] > value:
        # Shift L[j - 1] one position to the right to L[j].
        L[j] = L[j - 1]
        j = j - 1
    # Make room for the value by shifting.
    L[j] = value



def insertion_sort(L: list) -> None:
    """Sorts the items of L from smallest to largest using the
    insertion sort algorithm.
    
    >>> unsorted = [3, 5, 2, 1, 4]
    >>> insertion_sort(unsorted)
    >>> unsorted
    [1, 2, 3, 4, 5]
    
    >>> unsorted = [5, 3, 8, 6, 2, 1]
    >>> insertion_sort(unsorted)
    >>> unsorted
    [1, 2, 3, 5, 6, 8]
    """
    for i in range(1, len(L)):
        insert(L, i)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()