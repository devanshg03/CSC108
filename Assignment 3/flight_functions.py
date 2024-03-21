"""CSC108H1S: Functions for Assignment 3 - Airports and Routes.

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 The CSC108 Team
"""
from flight_constants import AirportDict, RouteDict, OPENFLIGHTS_NULL_VALUE

import flight_example_data


################################################################################
# Part 2 - Querying the data
################################################################################

def is_direct_flight(
        route_info: RouteDict,
        source: str, 
        destination: str) -> bool:
    """Return True if there is a direct flight from source to destination in
    RouteInfo, and False otherwise.

    Preconditions:
    - source in route_info
    - source and destination are formatted as IATA airport codes

    >>> example_routes = flight_example_data.create_example_routes()
    >>> is_direct_flight(example_routes, 'RCM', 'JCK')
    True
    >>> is_direct_flight(example_routes, 'JCK', 'TRO')
    False
    """
    return destination in route_info[source]


def is_valid_flight_sequence(route_info: RouteDict, flights: list[str]) -> bool:
    """Return True if the list of flights is a valid sequence of flights in
    route_info, and False otherwise.

    A valid sequence of flights is a list of flights where each flight is a
    direct flight from the previous destination to the next source.

    >>> example_routes = flight_example_data.create_example_routes()
    >>> is_valid_flight_sequence(example_routes, ['RCM', 'JCK', 'RCM'])
    True
    >>> is_valid_flight_sequence(example_routes, ['RCM', 'TRO', 'HKG'])
    False
    """
    if len(flights) < 2:
        return False
    for i in range(len(flights) - 1):
        if flights[i] not in route_info:
            return False
        if not is_direct_flight(route_info, flights[i], flights[i + 1]):
            return False
    return True


def summarize_by_timezone(airports: AirportDict) -> dict[str, int]:
    """Return a dictionary where the keys are the timezones given the timeszone
    is not null in airports and the values are the number of airports in
    airports that are in that timezone.

    >>> example_airports = flight_example_data.create_handout_airports()
    >>> summarize_by_timezone(example_airports)
    {'Australia/Sydney': 1, 'Australia/Brisbane': 1}
    """
    timezone_dict = {}
    for airport in airports:
        timezone = airports[airport]['Tz']
        if timezone != OPENFLIGHTS_NULL_VALUE:
            timezone_dict[timezone] = timezone_dict.get(timezone, 0) + 1
    return timezone_dict


################################################################################
# Part 3 - Implementing useful algorithms
################################################################################

def add_new_destinations(routes: RouteDict,
                         current_sources: list[str],
                         reachable_airports: list[str]) -> list[str]:
    """
    Returns a list of new destination airport codes to be used as current
    sources in the next iteration. Process current sources to find new
    destinations, updating the list of reachable airports.
    """
    new_sources = []
    for airport in current_sources:
        if airport in routes:
            for destination in routes[airport]:
                if (destination not in reachable_airports 
                        and destination not in current_sources):
                    new_sources.append(destination)
                    reachable_airports.append(destination)
    return new_sources


def find_reachable_destinations(routes: RouteDict, source: str, n: int) -> \
        list[str]:
    """Return the list of IATA airport codes that are reachable from source by
    taking at most n direct flights.

    The list should not contain an IATA airport code more than once. The airport
    codes in the list should appear in lexicographical order (use the
    list.sort method on a list of strings to achieve this).

    Preconditions:
        - n >= 1
        - (source in routes) is True

    >>> example_routes = flight_example_data.create_example_routes()
    >>> find_reachable_destinations(example_routes, 'GFN', 1)
    ['TRO']
    >>> find_reachable_destinations(example_routes, 'GFN', 2)
    ['GFN', 'SYD', 'TRO']
    """
    # Initialize the list of reachable airports and the list of current sources
    reachable_airports = []
    current_sources = [source]

    while n > 0:
        current_sources = add_new_destinations(routes,
                                               current_sources,
                                               reachable_airports)
        n -= 1
    return sorted(reachable_airports)


def decomission_plane(routes: RouteDict, plane: str) -> list[tuple[str, str]]:
    """Update routes by removing plane from all source-destination routes that
    use plane. Do not remove the source-destination pair, only the plane.

    In addition, return a sorted list of two-element tuples where the first
    index is source and the second index is destination (use the list.sort
    method on a list of tuples to achieve this). The list includes *all* routes
    that that have no planes that can be used.

    >>> example_routes = flight_example_data.create_example_routes()
    >>> decomission_plane(example_routes, 'DH4')
    []
    >>> example_routes['TRO']['SYD']
    ['SF3']
    >>> example_routes = flight_example_data.create_example_routes()
    >>> decomission_plane(example_routes, 'SF3')
    [('GFN', 'TRO'), ('JCK', 'RCM'), ('RCM', 'JCK'), ('TRO', 'GFN')]
    >>> example_routes['TRO']['SYD']
    ['DH4']
    """
    without_planes = []
    for source in routes:
        for destination in routes[source]:
            planes = routes[source][destination]
            if plane in planes:
                planes.remove(plane)
                if not planes:
                    without_planes.append((source, destination))
    return sorted(without_planes)


if __name__ == '__main__':
    # On A3 we do not have a separate checker but instead include code that
    # performs the required checks.  This code requires python_ta to be
    # installed.  See the 'Completing the CSC108 Setup' section in the
    # Software Installation page on Quercus for details.

    # Uncomment the 3 lines below to have function type contracts checked
    # # Enable type contract checking for the functions in this file
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    # Check the correctness of the doctest examples
    import doctest
    doctest.testmod()

    # Uncomment the 2 lines below to check your code style with python_ta
    import python_ta
    python_ta.check_all(config='pyta/a3_pyta.txt')
