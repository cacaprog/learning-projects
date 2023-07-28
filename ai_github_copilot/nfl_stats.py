""" 
open the csv file called "nfl_offensive_stats.csv" in the nfl_stats directory
and read in the csv data from the file
"""
import pandas as pd
data = pd.read_csv('nfl_stats/nfl_offensive_stats.csv')
print(data.head())

# print the columns names
print(data.columns)

""" 
In the data we just read in, the fourth column is the player
and the 8th column is the passing yards.  Get the sum of 
yards from column 8 where the 4th column value is
"Aaron Rodgers"
"""
print(data.loc[data['player'] == 'Aaron Rodgers', 'pass_yds'].sum())


"""
the 3rd column in data is player position, the fourth column 
is the player, and the 8th column is the passing yards. 
For each player whose position in column 3 is "QB", 
determine the sum of yards from column 8 
"""
print(data.loc[data['position '] == 'QB', 'pass_yds'].sum())

""" 
print the sum of the passing yards sorted by sum 
of passing yards in descending order
Do not include Tom Brady because he wins too much
group by player
"""
players_result = (data.loc[data['player'] != 'Tom Brady'].groupby('player')['pass_yds'].sum().sort_values(ascending=False))

"""

plot the players by their number of passing yards only for 
players with more than 4000 passing yards
"""
import matplotlib.pyplot as plt
payers_more = players_result.loc[players_result > 4000]
payers_more.plot(kind='bar')
plt.show()

      









