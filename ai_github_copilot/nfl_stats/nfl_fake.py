import doctest


def tot_pass_yds_player(input_file, player):

    """
    input_file is a string that is the name of a file
    player is the name of a player
    
    The file is a csv file with a header row
    Column 4 is the player's name and column
    8 is the number of passing yards for that player
  
    return the total number of passing yards for the player

    >>> tot_pass_yds_player('nfl_test_2.csv', 'Aaron Rodgers')
    800
    >>> tot_pass_yds_player('nfl_test_2.csv', 'Kerryon Johnson')
    5
    >>> tot_pass_yds_player('nfl_test_2.csv', 'Leo Porter')
    0
    >>> tot_pass_yds_player('nfl_test_2.csv', 'Dan Zingaro')
    -10
    >>> tot_pass_yds_player('nfl_test_2.csv', 'Jared Goff')
    190
    >>> tot_pass_yds_player('nfl_test_2.csv', 'Tom Brady')
    0 
    """
    
    import csv
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        total = 0
        for row in reader:
            if row[3] == player:
                total += int(row[7])
        return total
    
doctest.testmod(verbose=False)
