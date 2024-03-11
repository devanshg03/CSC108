from typing import TextIO, List, Dict, Tuple

"""
A restaurant recommendation system.

Example dictionaries that correspond to the information in restaurants_small.txt.

Restaurant name to rating:
# Dict[str, int]
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# Dict[str, List[str]]
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# Dict[str, List[str]]
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

#The file containing the restaurant data.
FILENAME = 'restaurants_small.txt'


def recommend(file: TextIO, price:str, cuisines_list: List[str]
              )-> List[List[str]]:
    """ Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structure:
    #  - Dict[restaurant name, rating%]
    #  - Dict[price, List[restaurant names]]
    #  - Dict[cuisine, List[restaurant names]]
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Look for price or cuisine first?
    # Price: Look up the list of restaurant names for the requested price.
    names_matching = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(
        names_matching, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range
    # and server the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, name_final)

    #We're done! Return that sorted list.
    return result


def build_rating_list(name_to_rating: Dict[str, int],
                      names_finals: List[str]) -> List[list]:
    """ Return a list of [rating%, restaurant name], sorted by rating %.

    >>> name_to_rating = {'Georgie Porgie': 87,
    'Queen St. Cafe': 82,
    'Dumplings R Us': 71,
    'Mexican Grill': 85,
    'Deep Fried Everything': 52}
    >>> names_final = ['Queen St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(name_to_rating, names_final)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

def filter_by_cuisine(names_matching: List[str],
                      cuisine_to_names: Dict[str, List[str]],
                      cuisines_list: List[str]) -> List[str]:
    """ 
    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = {'Canadian': ['Georgie Porgie'],
    'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
    'Malaysian': ['Queen St. Cafe'],
    'Thai': ['Queen St. Cafe'],
    'Chinese': ['Dumplings R Us'],
    'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """

def read_restaurants(file: TextIO) -> Tuple[Dict[str, int],
                                       Dict[str, List[str]],
                                       Dict[str, List[str]]]:
    """ Return a tuple of three dictionaries based on the information in file.

    - Dict[restaurant name, rating%]
    - Dict[price, List[restaurant names]]
    - Dict[cuisine, List[restaurant names]]
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    # Read the file and build the data structure.
    file = open(FILENAME, 'r')
    for line in file:
        line = line.strip()
        if line == '':
            continue
        elif line[0] == '$':
            price = line
        elif line[-1] == '%':
            name_to_rating[line[4:]] = int(line[:2])
        else:
            if line in cuisine_to_names:
                cuisine_to_names[line].append(line)
            else:
                cuisine_to_names[line] = [line]
            price_to_names[price].append(line)


if __name__ == '__main__':

    # with open(FILENAME, 'r') as f:
    #     print(recommend(f, '$', ['Chinese']))
    # with open(FILENAME, 'r') as f:
    #     print(recommend(f, '$$', ['Pub Food', 'Canadian']))
    # with open(FILENAME, 'r') as f:
    #     print(recommend(f, '$$$', ['Pub Food', 'Canadian']))
    with open(FILENAME, 'r') as f:
        print(recommend(f, '$', ['Chinese', 'Thai']))
