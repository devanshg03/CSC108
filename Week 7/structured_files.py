from typing import TextIO

def points_per_game(game_data: TextIO) -> list[list]:
    """Return a list containing the team name and the average number of points 
    earned per game for each team in the open file game_data. If the team has 
    no games, use None instead of an average number of points.

    >>> input_file = open('NHL-data.txt')
    >>> points_per_game(input_file)
    [['Toronto Maple Leafs', 1.17], ['Grande Prairie Storm', None], \
['Montreal Canadiens', 1.2]]
    >>> input_file.close()
    """
    
    result = []

    # read a line from the file to set up for the outer while loop condition
    line = game_data.readline().strip()
    while line != '': 
        # due to the structure of the file, line contains a team name.
        team_name = line
        # set up accumulator variables for the team.
        games_played = 0
        total_points = 0
        
        # read and process game points until new team name read 
        # or end of file reached
        ???
        
        # want this while loop to stop on a team name or end of file
        # want it to continue on points (digits)
        while ???:
            total_points = total_points + ???
            games_played = games_played + 1
            ???

        # add results for team_name 
        if ???:
            result.append([team_name, round(total_points / games_played, 2)])
        else:
            result.append([team_name, None])
            
    return result
