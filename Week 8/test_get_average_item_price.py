import pytest
from expenses import get_average_item_price   

    
def test_one_person_one_item() -> None:
    """Test one person with one expense.
    """
    actual = get_average_item_price({'Tom': [5.0]})
    expected = 5.0
    assert actual == expected
    

def test_one_person_many_items() -> None:
    """Test one person with many items.
    """
    actual = get_average_item_price({'Tom': [14.99, 3.25, 5.0]})
    expected = 7.746666666666666
    assert actual == expected
    
    
def test_many_people_with_one_item() -> None:
    """Test many people each with only one item.
    """ 
    
    
if __name__ == '__main__':
    pytest.main(['test_get_average_item_price.py'])