import unittest
from battleship_game_functions import (valid_cell_indexes, is_not_given_symbol, is_win,
                                       update_target_grid, update_fleet_grid,
                                       get_ship_symbol_count, has_ship,
                                       validate_symbol_counts, validate_ship_positions)
from battleship_game_functions import UNKNOWN, EMPTY, HIT, MISS

class TestBattleshipGameFunctions(unittest.TestCase):

    def test_valid_cell_indexes(self):
        self.assertTrue(valid_cell_indexes(2, 9, 10))
        self.assertFalse(valid_cell_indexes(2, 9, 9))
        # Boundary test
        self.assertTrue(valid_cell_indexes(0, 0, 10))
        self.assertTrue(valid_cell_indexes(9, 9, 10))
        self.assertFalse(valid_cell_indexes(10, 10, 10))
        # Minimum test
        self.assertTrue(valid_cell_indexes(0, 0, 1))
        self.assertFalse(valid_cell_indexes(1, 1, 1))
        # Negative test
        self.assertFalse(valid_cell_indexes(-1, -1, 10))

    def test_is_not_given_symbol(self):
        my_grid = [['a', '-'], ['-', 'b']]
        self.assertTrue(is_not_given_symbol(1, 1, my_grid, UNKNOWN))
        self.assertFalse(is_not_given_symbol(0, 1, my_grid, UNKNOWN))
        # Test with different symbol
        grid = [['X', 'O'], ['1', '*']]
        self.assertTrue(is_not_given_symbol(0, 1, grid, 'X'))
        self.assertFalse(is_not_given_symbol(1, 0, grid, '1'))
        # Test with grid corners
        grid = [['a', 'b'], ['c', 'd']]
        self.assertTrue(is_not_given_symbol(0, 0, grid, 'b'))
        self.assertTrue(is_not_given_symbol(1, 1, grid, 'c'))
        # Test with different grid sizes
        small_grid = [['X']]
        large_grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertFalse(is_not_given_symbol(0, 0, small_grid, 'X'))
        self.assertTrue(is_not_given_symbol(2, 2, large_grid, '5'))

    def test_is_win(self):
        self.assertTrue(is_win([1, 2, 3], [1, 2, 3]))
        self.assertFalse(is_win([1, 2, 3], [1, 2, 0]))

    def test_update_target_grid(self):
        my_target_grid = [[UNKNOWN, UNKNOWN], [UNKNOWN, UNKNOWN]]
        their_fleet_grid = [['a', 'b'], ['a', EMPTY]]
        update_target_grid(1, 1, my_target_grid, their_fleet_grid)
        self.assertEqual(my_target_grid, [[UNKNOWN, UNKNOWN], [UNKNOWN, MISS]])

        my_target_grid = [[UNKNOWN, UNKNOWN], [UNKNOWN, UNKNOWN]]
        their_fleet_grid = [[EMPTY, EMPTY], [EMPTY, 'a']]
        update_target_grid(1, 1, my_target_grid, their_fleet_grid)
        self.assertEqual(my_target_grid, [[UNKNOWN, UNKNOWN], [UNKNOWN, HIT]])

    def test_update_fleet_grid(self):
        my_hits_list = [0]
        my_fleet_grid = [[EMPTY, 'a'], [EMPTY, 'a']]
        update_fleet_grid(0, 1, my_fleet_grid, ['a'], my_hits_list)
        self.assertEqual(my_hits_list, [1])
        self.assertEqual(my_fleet_grid, [[EMPTY, 'A'], [EMPTY, 'a']])

    def test_get_ship_symbol_count(self):
        grid = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
        self.assertEqual(get_ship_symbol_count(grid, 'c'), 3)
        grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'i', 'j']]
        self.assertEqual(get_ship_symbol_count(grid, 'k'), 0)

    def test_has_ship(self):
        grid = [[EMPTY, 'b', EMPTY], ['a', 'b', EMPTY], [EMPTY, EMPTY, EMPTY]]
        self.assertTrue(has_ship(grid, 0, 1, 'b', 2))
        self.assertFalse(has_ship(grid, 0, 1, 'b', 1))
        self.assertFalse(has_ship(grid, 0, 1, 'b', 3))
        self.assertTrue(has_ship(grid, 1, 0, 'a', 1))
        grid = [['b', 'b', 'b'], ['b', EMPTY, EMPTY], ['b', EMPTY, EMPTY]]
        self.assertFalse(has_ship(grid, 0, 0, 'b', 3))

    def test_validate_symbol_counts(self):
        grid = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY], ['a', 'a', 'a']]
        ships = ['a', 'b']
        sizes = [3, 2]
        self.assertTrue(validate_symbol_counts(grid, ships, sizes))
        grid = [['b', EMPTY, EMPTY], [EMPTY, 'b', 'a'], ['a', 'a', EMPTY]]
        self.assertTrue(validate_symbol_counts(grid, ships, sizes))
        grid = [['d', 'a', 'n'], [EMPTY, 'i', 's'], ['f', 'i', 't']]
        ships = ['a', 'd', 'f', 'i', 'n']
        sizes = [1, 1, 1, 2, 1]
        self.assertFalse(validate_symbol_counts(grid, ships, sizes))

    def test_validate_ship_positions(self):
        grid = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY], ['a', 'a', 'a']]
        ships = ['a', 'b']
        sizes = [3, 2]
        self.assertTrue(validate_ship_positions(grid, ships, sizes))
        grid = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY], ['a', 'b', 'a']]
        ships = ['a', 'b']
       
if __name__ == '__main__':
    unittest.main()