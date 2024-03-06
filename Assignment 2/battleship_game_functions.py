"""CSC108: Winter 2024 -- Assignment 2: Battleship Game

module: battleship_game_functions

This code is provided solely for the personal and private use of
students taking the course CSC108/CSCA08 at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this folder and all subfolders are:
Copyright (c) 2024 The CSC108/CSCA08 Team
"""

# Constants that describe the limits on ship sizes and grid sizes.
MIN_SHIP_SIZE = 1
MAX_SHIP_SIZE = 10
MAX_GRID_SIZE = 10

# Constants that describe valid grid cell values (other than ship symbols).
EMPTY = '.'
UNKNOWN = '-'
HIT = 'X'
MISS = 'M'


# Implement the required functions below according to their docstrings.
#
# We have provided the complete docstring (but not the body!) for each of the
# functions that you are to complete.  When you have completed all of the
# functions, run the file play_battleship_game.py to play the game!


def valid_cell_indexes(row: int, col: int, grid_size: int) -> bool:
    """Return True if and only if row and col are between 0 (inclusive) and
    grid_size (non-inclusive).

    >>> valid_cell_indexes(2, 9, 10)
    True
    >>> valid_cell_indexes(2, 9, 9)
    False
    """
    return (0 <= row < grid_size) and (0 <= col < grid_size)


def is_not_given_symbol(row: int, col: int, grid: list[list[str]],
                        symbol: str) -> bool:
    """Return True if and only if the grid cell with row position row and
    column position col is NOT symbol.

    Preconditions:
        - 0 <= row < len(grid)
        - 0 <= col < len(grid)
        - 0 < len(grid)
        - len(grid[i]) == len(grid)
              for each value of i in range(len(grid))

    >>> my_grid = [['a', UNKNOWN], [UNKNOWN, 'b']]
    >>> is_not_given_symbol(1, 1, my_grid, UNKNOWN)
    True
    >>> is_not_given_symbol(0, 1, my_grid, UNKNOWN)
    False
    """
    return grid[row][col] != symbol


def is_win(ship_sizes: list[int], hits_list: list[int]) -> bool:
    """Return True if and only if hits_list contains the same values as
    ship_sizes, in the same order.

    ship_sizes and hits_list are parallel lists.

    Preconditions:
       - len(ship_sizes) == len(hits_list)

    >>> is_win([1, 2, 3], [1, 2, 3])
    True
    >>> is_win([1, 2, 3], [1, 2, 0])
    False
    """
    for i in range(len(ship_sizes)):
        if ship_sizes[i] != hits_list[i]:
            return False
    return True


def update_target_grid(row: int, col: int, target_grid: list[list[str]],
                       fleet_grid: list[list[str]]) -> None:
    """Modify the cell with row position row and column position col in
    target_grid to either HIT or MISS by using the information in the
    corresponding cell from fleet_grid.

    Preconditions:
        - 0 <= row < len(target_grid)
        - 0 <= col < len(target_grid)
        - 0 < len(target_grid)
        - len(target_grid[i]) == len(target_grid)
              for each value of i in range(len(target_grid))
        - len(fleet_grid) == len(target_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))

    >>> my_target_grid = [[UNKNOWN, UNKNOWN], [UNKNOWN, UNKNOWN]]
    >>> their_fleet_grid = [['a', 'b'], ['a', EMPTY]]
    >>> update_target_grid(1, 1, my_target_grid, their_fleet_grid)
    >>> my_target_grid == [[UNKNOWN, UNKNOWN], [UNKNOWN, MISS]]
    True
    >>> my_target_grid = [[UNKNOWN, UNKNOWN], [UNKNOWN, UNKNOWN]]
    >>> their_fleet_grid = [[EMPTY, EMPTY], [EMPTY, 'a']]
    >>> update_target_grid(1, 1, my_target_grid, their_fleet_grid)
    >>> my_target_grid == [[UNKNOWN, UNKNOWN], [UNKNOWN, HIT]]
    True
    """
    if is_not_given_symbol(row, col, fleet_grid, EMPTY):
        target_grid[row][col] = HIT
    else:
        target_grid[row][col] = MISS


def update_fleet_grid(row: int, col: int, fleet_grid: list[list[str]],
                      ship_symbols: list[str], hits_list: list[int]) -> None:
    """Modify hits_list and fleet_grid to account for a hit of the cell
    at row position row and column position col.  Convert the correct cell
    in fleet_grid to upper case and increase the corresponding count in
    hits_list by one.

    ship_symbols and hits_list are parallel lists.

    Preconditions:
        - 0 <= row < len(fleet_grid)
        - 0 <= col < len(fleet_grid)
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - len(ship_symbols) == len(hits_list) and 0 < len(ship_symbols)
        - fleet_grid[row][col] in ship_symbols

    >>> my_hits_list = [0]
    >>> my_fleet_grid = [[EMPTY, 'a'], [EMPTY, 'a']]
    >>> update_fleet_grid(0, 1, my_fleet_grid, ['a'], my_hits_list)
    >>> my_hits_list == [1]
    True
    >>> my_fleet_grid == [[EMPTY, 'A'], [EMPTY, 'a']]
    True
    """
    ship_index = ship_symbols.index(fleet_grid[row][col])
    fleet_grid[row][col] = fleet_grid[row][col].upper()
    hits_list[ship_index] += 1


def get_ship_symbol_count(fleet_grid: list[list[str]],
                          ship_symbol: str) -> int:
    """Return the number of occurrences of ship_symbol in fleet_grid.

    Preconditions:
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - len(ship_symbol) == 1

    >>> grid = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
    >>> get_ship_symbol_count(grid, 'c')
    3
    >>> grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'i', 'j']]
    >>> get_ship_symbol_count(grid, 'k')
    0
    """
    return sum(row.count(ship_symbol) for row in fleet_grid)


def has_ship(fleet_grid: list[list[str]], row_start: int, col_start: int,
             ship_symbol: str, ship_size: int) -> bool:
    """Return True if and only if a ship that (1) uses ship_symbol as its ship
    symbol and (2) has length ship_size appears in fleet_grid starting at
    position (row_start, col_start), where (row_start, col_start) is the
    top-most/left-most corner of the ship.

    If the ship has ship_size 2 or more and appears as both a column and a row,
    return False.

    Preconditions:
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - 0 <= row_start < len(fleet_grid)
        - 0 <= col_start < len(fleet_grid)
        - MIN_SHIP_SIZE <= ship_size <= MAX_SHIP_SIZE
        - fleet_grid[i][j] != ship_symbol for each of the coordinates
             (i, j) == (row_start - 1, col_start) or
             (i, j) == (row_start, col_start - 1)
             when those coordinates are valid indexes for fleet_grid
 
    >>> grid = [[EMPTY, 'b', EMPTY], ['a', 'b', EMPTY], [EMPTY, EMPTY, EMPTY]]
    >>> has_ship(grid, 0, 1, 'b', 2)
    True
    >>> has_ship(grid, 0, 1, 'b', 1)
    False
    >>> has_ship(grid, 0, 1, 'b', 3)
    False
    >>> has_ship(grid, 1, 0, 'a', 1)
    True
    >>> grid = [['b', 'b', 'b'], ['b', EMPTY, EMPTY], ['b', EMPTY, EMPTY]]
    >>> has_ship(grid, 0, 0, 'b', 3)
    False
    """
    # Check if the length of the ship is correct
    if get_ship_symbol_count(fleet_grid, ship_symbol) != ship_size:
        return False
    
    # Check if ship of size one is in the grid
    if ship_size == 1:
        return fleet_grid[row_start][col_start] == ship_symbol
    # Check if ship of size two or above is in the grid in a row or column
    else:
        # Check if the ship is a row
        # Get the range of the row to search
        row_search_range = min(
            col_start + ship_size,
            len(fleet_grid[row_start]))

        in_row = True
        match_count = 0
        for i in range(col_start, row_search_range):
            if fleet_grid[row_start][i] != ship_symbol:
                in_row = False
            else:
                match_count += 1
        if match_count != ship_size:
            in_row = False

        # Check if the ship is a column
        # Get the range of the column to search
        col_search_range = min(
            row_start + ship_size,
            len(fleet_grid))
        
        in_col = True
        match_count = 0
        for i in range(row_start, col_search_range):
            if fleet_grid[i][col_start] != ship_symbol:
                in_col = False
            else:
                match_count += 1
        if match_count != ship_size:
            in_col = False
        
        # Checks if ship of size two or above is both in a row and a column
        if in_row and in_col:
            return False
        # Returns if the ship is in either a row or a column
        return in_row or in_col


def validate_symbol_counts(fleet_grid: list[list[str]],
                           ship_symbols: list[str],
                           ship_sizes: list[int]) -> bool:
    """Return True if and only if fleet_grid contains each ship symbol in
    ship_symbols the correct corresponding number of times from ship_sizes,
    and nothing else except for the EMPTY character.

    ship_symbols and ship_sizes are parallel lists.

    Note: This function does not consider whether ship symbols are positioned
    in an appropriate manner to form a complete ship.  It simply validates the
    symbol counts.

    Preconditions:
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - len(ship_symbols) == len(ship_sizes) and 0 < len(ship_symbols)
        - len(ship_symbols[i]) == 1
              for each value of i in range(len(ship_symbols))
        - 1 <= len(ship_sizes[i])
              for each value of i in range(len(ship_sizes))

    >>> grid = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY], ['a', 'a', 'a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> validate_symbol_counts(grid, ships, sizes)
    True
    >>> grid = [['b', EMPTY, EMPTY], [EMPTY, 'b', 'a'], ['a', 'a', EMPTY]]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> validate_symbol_counts(grid, ships, sizes)
    True
    >>> grid = [['d', 'a', 'n'], [EMPTY, 'i', 's'], ['f', 'i', 't']]
    >>> ships = ['a', 'd', 'f', 'i', 'n']
    >>> sizes = [1, 1, 1, 2, 1]
    >>> validate_symbol_counts(grid, ships, sizes)
    False
    """
    for i in range(len(ship_symbols)):
        if get_ship_symbol_count(fleet_grid, ship_symbols[i]) != ship_sizes[i]:
            return False

    for row in fleet_grid:
        for col in row:
            if col not in ship_symbols and col != EMPTY:
                return False
    return True


def validate_ship_positions(fleet_grid: list[list[str]],
                            ship_symbols: list[str],
                            ship_sizes: list[int]) -> bool:
    """Return True if and only if fleet_grid contains each ship in ship_symbols
    the correct corresponding number of times from ship_sizes, with ship
    characters all connected in a single row or column.

    ship_symbols and ship_sizes are parallel lists.

    Preconditions:
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - len(ship_symbols) == len(ship_sizes) and 0 < len(ship_symbols)
        - len(ship_symbols[i]) == 1
              for each value of i in range(len(ship_symbols))
        - 1 <= len(ship_sizes[i])
              for each value of i in range(len(ship_sizes))
        - validate_symbol_counts(fleet_grid, ship_symbols, ship_sizes) == TRUE

    >>> grid = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY], ['a', 'a', 'a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> validate_ship_positions(grid, ships, sizes)
    True
    >>> grid = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY], ['a', 'b', 'a']]
    >>> ships = ['a', 'b']
    >>> sizes = [2, 3]
    >>> validate_ship_positions(grid, ships, sizes)
    False
    """ 
    ship_found = [False] * len(ship_symbols)

    for ship, size in zip(ship_symbols, ship_sizes):
        ship_index = ship_symbols.index(ship)

        # Check if each ship is contained the correct number of times
        if get_ship_symbol_count(fleet_grid, ship) != size:
            return False

        # Check if all ship is connected in a single row or column
        for row in range(0, len(fleet_grid)):
            for col in range(0, len(fleet_grid)):
                if (fleet_grid[row][col] == ship and
                    not ship_found[ship_index] and
                        has_ship(fleet_grid, row, col, ship, size)):
                    ship_found[ship_index] = True
    return all(ship_found)


if __name__ == '__main__':
    # Automatically run all doctest examples to see if any fail
    import doctest
    # uncomment the line below to run the docstring examples
    doctest.testmod()
