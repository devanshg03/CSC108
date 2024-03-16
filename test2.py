def mystery(lst1: list, lst2: list) -> None:
    """
    Sets every item in the sublist of lst1 that are also in lst2 to 0.
    """
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            if lst1[i][j] in lst2:
                lst1[i][j] = 0


def get_incompatibility_dict(data: list) -> dict:
    """
    Given compatibility `data` where each element is of the form (N1, N2, BOOL),
    build and return a dictionary where each number is a key associated with a list
    value containing all of that number's incompatible numbers, like so:

    {n1: [all incompatible nums for n1],
     n2: [all incompatible nums for n2],
        ... 
     }
    
    >>> test_list = [(1, 2, False), (1, 1, False), (1, 4, True)]
    >>> get_incompatibility_dict(test_list)
    {1: [2, 1]}
    
    >>> test_list = [(1, 2, True), (1, 1, True), (2, 3, True), (3, 4, False), (3, 2, False)]
    >>> get_incompatibility_dict(test_list)
    {3: [4, 2]}
    """
    d = {}
    for tup in data:
        n = tup[0]
        m = tup[1]
        compatible = tup[2]

        if not compatible:
            if n in d:
                d[n].append(m)
            else:
                d[n] = [m]
    return d

def check_same_group(file, name1: str, name2: str) -> bool:
    """ Given an open file containing group information, return whether name1 and name2 occur in the same group.
    
    Every group is divided by a *** line.
    
    Preconditions:
    - the file has at least one group
    - all group member names are unique
    - all names in the file, and name1 and name2, contain only lowercase letters
    
    >>> file = open('../sample_groups.txt')
    >>> check_same_group(file, 'sadia', 'paul')
    True
    >>> check_same_group(file, 'yun', 'tom')
    False
    """
    line = file.readline().strip()
    while line != '':
        current_group = []
        while line != '***':
            current_group.append(line)
            line = file.readline().strip()
        if name1 in current_group and name2 in current_group:
            return True
        line = file.readline().strip()
    return False

def mystery_v2(lst: list[list[int]], n1: int, n2: int) -> None:
    """
    Replaces every instance of n1 in the sublists of lst with n2.

    >>> L = [[1, 2, 3], [2, 45, 22]]
    >>> mystery_v2(L, 2, 99)
    >>> L
    [[1, 99, 3], [99, 45, 22]]

    >>> L = [[1, 2, 3], [2, 45, 22]]
    >>> mystery_v2(L, 20, 99)
    >>> L
    [[1, 2, 3], [2, 45, 22]]
    """
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == n1:
                lst[i][j] = n2
def build_numerology_dict(data: list[list]) -> dict[int, tuple[list[int]]]:
    """
    Given compatibility `data` where each element is of the form [N1, N2, BOOL], build and return a dictionary with the following structure:
        
        {
            n1: ([all compatible nums for n1], [all incompatible nums for n1]),
            n2: ([all compatible nums for n2], [all incompatible nums for n2]),
            ...
        }

    >>> test_list = [[1, 2, True], [1, 1, True], [1, 4, False], [2, 3, True], [3, 1, True], [3, 2, False]]
    >>> build_numerology_dict(test_list)
    {1: ([2, 1], [4]), 2: ([3], []), 3: ([1], [2])}
    """
    d = {}
    for sublst in data:
        n = sublst[0]
        m = sublst[1]
        compatible = sublst[2]

        if n not in d:
            d[n] = ([], [])
        if compatible:
            d[n][0].append(m)
        else:
            d[n][1].append(m)
    return d

def count_members(file) -> list[int]:
    """
    "Given an open file containing group information as described above,return a list containing the number of people in each group.
    
    Every group begins with a GROUP # line (where # is the number for that group).
    All member names contain only lower-case letters.

    Precondition:
    - the file has at least one group
    
    >>> file = open('../example_groups.txt')
    >>> count_members(file)
    [2, 3, 1]
    """
    counts = []
    line = file.readline().strip()
    while line != '':
        group_count = 0
        line = file.readline().strip()
        while line != '' and 'GROUP' not in line:
            group_count += 1
            line = file.readline().strip()
        counts.append(group_count)
    return counts
