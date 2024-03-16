"""Week 9 Perform - Part 2"""

# file name: w09_markus.py
# also needs file: fluffy_functions.py to be in the same folder
#
# Complete the following steps:
# (1) In addition to this file, download and open 
#     fluffy_functions.py in Wing101.
# (2) Review the test cases you chose for the all_fluffy function as part of 
#     the Choosing Test Cases exercise in the Week 9 lectures.
# (3) Implement the test cases you chose as test functions below.
#     Make sure you save your file regularly.
# (4) Run your tests on the correct version of all_fluffy from the 
#     fluffy_functions.py file, where it is named all_fluffy_v0.  We have
#     provided an import statement below to help you do that.  Make sure your
#     tests all run and pass when the correct code is provided.
# (5) Run your tests on the buggy versions of all_fluffy from the 
#     fluffy_functions.py file. The simplest way to do that is to make the
#     first import statement that we have provided into a comment, and then
#     uncomment one of the import statements that follow.  To test a different
#     buggy version of all_fluffy, uncomment a different import statement.
# (6) When convinced that your tests are complete, submit your modified
#     w09_markus.py file to MarkUs. You can find instructions on submitting a
#     file to MarkUs in the Week *2* Perform -> Accessing Part 2 of the
#     Week 2 Perform (For Credit) on PCRS.
# (7) Verify you have submit the right file to MarkUs by downloading it again
#     and checking it is the one you meant to submit.
# (8) We have also provided a checker test for you to run in MarkUs. This week
#     the checker runs your tests on a correct version of the all_fluffy
#     function.  We will not be marking your style on this exercise, so there
#     will be no PyTA check. We will run additional tests with different
#     versions of buggy code when we mark your submission to determine whether
#     your test suite is complete.
#
# NOTE: **Restart the Python shell** before running this module to ensure that
#       the desired all_fluffy function is imported and called.  Do this shell
#       restart each time you run this module.

import pytest

# Uncomment ONE of the following "from fluffy_functions" statements, depending
# on which version of all_fluffy you wish to test. Only add/delete the comment
# (#) symbol and blank.

# For running the checker on MarkUs, uncomment the _v0 version and comment out
# the other "from fluffy_functions" statements.

from fluffy_functions import all_fluffy_v0 as all_fluffy

# from fluffy_functions import all_fluffy_v1 as all_fluffy
# from fluffy_functions import all_fluffy_v2 as all_fluffy
# from fluffy_functions import all_fluffy_v3 as all_fluffy


def test_empty_string() -> None:
    """Test that the empty string is fluffy."""
    expected = True
    actual = all_fluffy('')
    assert actual == expected


# Add your other test methods below:
def test_all_fluffy() -> None:
    """Test that a string with all fluffy letters is fluffy."""
    expected = True
    actual = all_fluffy('fluffy')
    assert actual == expected

def test_repeated_fluffy() -> None:
    """Test that a string with repeated fluffy letters is fluffy."""
    expected = True
    actual = all_fluffy('fflluuffyy')
    assert actual == expected

def test_mixed_case() -> None:
    """Test that a string with mixed case letters is not fluffy."""
    expected = False
    actual = all_fluffy('FlUfFy')
    assert actual == expected

def test_upper_case() -> None:
    """Test that a string with upper case fluffy letters is not fluffy."""
    expected = False
    actual = all_fluffy('FLUFFY')
    assert actual == expected

def test_only_non_fluffy() -> None:
    """Test that a string with non-fluffy letters is not fluffy."""
    expected = False
    actual = all_fluffy('abcde')
    assert actual == expected

def test_mixed_fluffy() -> None:
    """Test that a string with mixed fluffy and non-fluffy letters is not fluffy."""
    expected = False
    actual = all_fluffy('fluffyaba')
    assert actual == expected

def test_numeric() -> None:
    """Test that a string with numeric characters is not fluffy."""
    expected = False
    actual = all_fluffy('12345fl')
    assert actual == expected

def test_special_characters() -> None:
    """Test that a string with special characters is not fluffy."""
    expected = False
    actual = all_fluffy('@fluff')
    assert actual == expected

def test_whitespace() -> None:
    """Test that a string with whitespace is not fluffy."""
    expected = False
    actual = all_fluffy(' fluffy ')
    assert actual == expected

def test_only_whitespace() -> None:
    """Test that a string with only whitespace is not fluffy."""
    expected = False
    actual = all_fluffy(' ')
    assert actual == expected

def test_unique_fluffy_different_order() -> None:
    """Test that a string with all unique fluffy letters in a different order is fluffy."""
    expected = True
    actual = all_fluffy('yffluf')
    assert actual == expected

def test_lower_case_fluffy() -> None:
    """Test that a string with lower case fluffy letters is fluffy."""
    expected = True
    actual = all_fluffy('fluffy')
    assert actual == expected

def test_non_english_characters() -> None:
    """Test that a string with non-English characters is not fluffy."""
    expected = False
    actual = all_fluffy('flüffy')
    assert actual == expected

def test_single_fluffy_character() -> None:
    """Test that a single fluffy character is considered fluffy."""
    expected = True
    actual = all_fluffy('f')
    assert actual == expected

def test_long_string_with_mixed_characters() -> None:
    """Test a long string containing both fluffy and non-fluffy characters."""
    expected = False
    actual = all_fluffy('ffluffylongstringwithnonfluffyx')
    assert actual == expected

def test_unique_fluffy_letters() -> None:
    """Test a string that contains all unique fluffy letters."""
    expected = True
    actual = all_fluffy('fuly')
    assert actual == expected

if __name__ == '__main__':
    pytest.main(['w09_markus.py'])
