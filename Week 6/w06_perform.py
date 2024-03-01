def average_daily_temp(high_temps: list[int],
                       low_temps: list[int]) -> list[float]:
    """high_temps and low_temps are daily high and low temperatures for a series
    of days. Return a new list of temperatures where each item is the daily
    average.

    Precondition: len(high_temps) == len(low_temps)
   
    >>> average_daily_temp([26, 27, 27, 28, 27, 26], [20, 20, 20, 20, 21, 21])
    [23.0, 23.5, 23.5, 24.0, 24.0, 23.5]
    """
    return [(high_temps[i] + low_temps[i]) / 2 for i in range (len(high_temps))]

def warmer_year(temps_then: list[int], temps_now: list[int]) -> list[str]:
    """Return a list of strings representing whether this year's 
    temperatures from temps_now are warmer than past temperatures
    in temps_then. The resulting list should contain "Warmer" at the
    indexes where this year's temperature is warmer, and "Not Warmer"
    at the indexes where the past year was warmer, or there is a tie.

    Precondition: len(temps_then) == len(temps_now)
   
    >>> warmer_year([10], [11])
    ['Warmer']
    >>> warmer_year([26, 27, 27, 28], [25, 28, 27, 30])
    ['Not Warmer', 'Warmer', 'Not Warmer', 'Warmer']
    """
    return [("Warmer" if temps_then[j] < temps_now[j] else "Not Warmer") for j in range(len(temps_now))]