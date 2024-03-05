from underperformers import collect_underperformers

# Note: this test suite does not contain a complete set of test cases.


def test_low_threshold() -> None:
    """ Test collect_underperformers with a threshold for which there
    are no underperformers."""

    actual_underperformers = collect_underperformers([4, 5, 6], 1)
    expected_underperformers = []
    assert actual_underperformers == expected_underperformers


def test_high_threshold() -> None:
    """ Test collect_underperformers with a threshold for which all items
    are underperformers."""



def test_mutation() -> None:
    """ Confirm that collect_underperformers does not mutate the list it's given."""



if __name__ == '__main__':
    import pytest
    pytest.main(['test_collect_underperformers.py'])
        
        
