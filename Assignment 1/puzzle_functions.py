""" Where's That Word? functions. """

# This file starts with the setting up of some constant variables and some
# helper functions that are provided to students, and ends with a part of
# the first function that students are to complete.
#
# Some of the programming techniques used in the provided helper functions
# have not been taught yet.  Students may read the docstrings to determine what
# these functions do and how to use them.

# Constants that describe the valid directions.  These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# Constants that describe the multiplicative factor used when scoring a
# word in a particular direction.  This should be used in function get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# Constants that describe the threshold for scoring.  This should be
# used in function get_points.
THRESHOLD = 5
BONUS = 12

# Constants that describe the two players and the result of the game.  These
# should be used as return values in functions get_current_player and
# get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# Constants that describe which puzzle to play.  Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.
# Do NOT modify these.
# You are welcome to call them in the function bodies that you write.


def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Preconditions:
       -  0 <= col_num < number of columns in puzzle
       -  puzzle is in the proper 'Where's that word?' puzzle format

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    >>> get_column('abcd\nefgh\nijkl\n', 0)
    'aei'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column = column + row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    Preconditions:
       -  puzzle is in the proper 'Where's that word?' puzzle format

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    >>> get_row_length('ab\ncd\nef\n')
    2
    """

    return len(puzzle.split('\n')[0])


def string_contains(text1: str, text2: str) -> bool:
    """Return True if and only if text2 appears anywhere in text1.

    >>> string_contains('abc', 'bc')
    True
    >>> string_contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.
#
# We have provided the complete docstring (but not the body!) for the first
# function you are to write.  Write a function body for the function
# get_current_player and then follow the Function Design Recipe to produce
# complete functions for get_winner, get_factor, reverse, get_row, get_points
# and check_guess.  When you have completed all of these functions, run the
# file puzzle_program.py to play the game!


def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' if and only if player_one_turn is True; otherwise,
    return 'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """
    return P1 if player_one_turn else P2
    # Complete this function.

# Now complete the functions:
# get_winner, get_factor, reverse, get_row, get_points and check_guess


def get_winner(player_one_score: int, player_two_score: int) -> str:
    """Compares the player_one_score and player_two_score and returns the winner
    of the game; otherwise, returns 'tie game' if the scores are equal.
    
    >>> get_winner(10, 20)
    'player two wins'

    >>> get_winner(20, 10)
    'player one wins'

    >>> get_winner(10, 10)
    'tie game'
    """
    if player_one_score > player_two_score:
        return P1_WINS
    elif player_one_score < player_two_score:
        return P2_WINS
    else:
        return TIE


def get_factor(direction: str) -> int:
    """Returns the multiplicative factor associated with the direction.
    
    >>> get_factor('up')
    4
    
    >> get_factor('backward')
    3
    """
    if direction == 'up':
        return UP_FACTOR
    elif direction == 'down':
        return DOWN_FACTOR
    elif direction == 'forward':
        return FORWARD_FACTOR
    else:
        return BACKWARD_FACTOR


def reverse(string: str) -> str:
    """ Returns the reverse of string.
    
    >>> reverse('nice')
    'ecin'
    
    >>> reverse('hello')
    'olleh'
    """
    return string[::-1]


def get_row(puzzle: str, row: int) -> str:
    """ Finds the row in puzzle and returns the string in the row.
    
    Preconditions:
       -  puzzle is in the proper 'Where's that word?' puzzle format
    
    >>> get_row('abcd\nefgh\nijkl\n',1)
    'efgh'
    
    >>> get_row('abcd\nefgh\nijkl\n',2)
    'ijkl'
    """
    return puzzle.split('\n')[row]


def get_points(direction: str, words_left: int) -> int:
    """
    Returns the points earned when a word is found in direction when word_left
    are remaning.
    
    >>> get_points('backward', 5)
    15
    
    >>> get_points('backward', 3)
    21
    
    >>> get_points('backward', 1)
    39
    """
    factor = get_factor(direction)
    
    if words_left >= THRESHOLD:
        return THRESHOLD * factor
    elif words_left == 1:
        return (2 * THRESHOLD - words_left) * factor + BONUS
    else:
        return (2 * THRESHOLD - words_left) * factor


def check_guess(puzzle: str, direction: str, guess: str, row_or_col_num: int, 
                words_left: int) -> int:
    """
    Returns the number of points earned if guess is found in row_or_col_num of 
    puzzle; Otherwise, returns 0.
    
    (Examples not included since function produces output and takes input.)
    """
    guess_r = reverse(guess)
    
    if direction in (FORWARD, BACKWARD):
        line = get_row(puzzle, row_or_col_num)
    elif direction in (DOWN, UP):
        line = get_column(puzzle, row_or_col_num)
        
    if direction in (FORWARD, DOWN):
        if string_contains(line, guess):
            return get_points(direction, words_left)
        else:
            return 0
    else:
        if string_contains(line, guess_r):
            return get_points(direction, words_left)
        else:
            return 0
