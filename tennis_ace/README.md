“Game, Set, Match!”

No three words are sweeter to hear as a tennis player than those, which indicate that a player has beaten their opponent. While you can head down to your nearest court and aim to overcome your challenger across the net without much practice, a league of professionals spends day and night, month after month practicing to be among the best in the world. Today you will put your linear regression knowledge to the test to better understand what it takes to be an all-star tennis player.

Provided in tennis_stats.csv is data from the men’s professional tennis league, which is called the ATP (Association of Tennis Professionals). Data from the top 1500 ranked players in the ATP over the span of 2009 to 2017 are provided in file. The statistics recorded for each player in each year include service game (offensive) statistics, return game (defensive) statistics and outcomes. 

1. Load the csv into a DataFrame and investigate it to gain familiarity with the data.

Player
438 unique - os nomes se repetem, pois mostra os resultados do jogador pelos anos
Year: 2009 a 2017

**Identifying Data**

    Player: name of the tennis player
    Year: year data was recorded (from 2009 to 2017)

**Service Game Columns (Offensive)**

    Aces: number of serves by the player where the receiver does not touch the ball
    DoubleFaults: number of times player missed both first and second serve attempts
    FirstServe: % of first-serve attempts made
    FirstServePointsWon: % of first-serve attempt points won by the player
    SecondServePointsWon: % of second-serve attempt points won by the player
    BreakPointsFaced: number of times where the receiver could have won service game of the player
    BreakPointsSaved: % of the time the player was able to stop the receiver from winning service game when they had the chance
    ServiceGamesPlayed: total number of games where the player served
    ServiceGamesWon: total number of games where the player served and won
    TotalServicePointsWon: % of points in games where the player served that they won

**Return Game Columns (Defensive)**

    FirstServeReturnPointsWon: % of opponents first-serve points the player was able to win
    SecondServeReturnPointsWon: % of opponents second-serve points the player was able to win
    BreakPointsOpportunities: number of times where the player could have won the service game of the opponent
    BreakPointsConverted: % of the time the player was able to win their opponent’s service game when they had the chance
    ReturnGamesPlayed: total number of games where the player’s opponent served
    ReturnGamesWon: total number of games where the player’s opponent served and the player won
    ReturnPointsWon: total number of points where the player’s opponent served and the player won
    TotalPointsWon: % of points won by the player

**Outcomes**

    Wins: number of matches won in a year
    Losses: number of matches lost in a year
    Winnings: total winnings in USD($) in a year
    Ranking: ranking at the end of year


3. Perform exploratory analysis on the data by plotting different features against the different outcomes. What relationships do you find between the features and outcomes? Do any of the features seem to predict the outcomes?

**Strong correlations**
Wins: ServiceGamesPlayed, ReturnGamesPlayed, DoubleFaults, BreakPointsOpportunities, BreakPointsFaced, Aces

4. Use one feature from the dataset to build a single feature linear regression model on the data. Your model, at this point, should use only one feature and predict one of the outcome columns. Before training the model, split your data into training and test datasets so that you can evaluate your model on the test set. How does your model perform? 

Plot your model’s predictions on the test set against the actual outcome variable to visualize the performance.


5. Create a few more linear regression models that use one feature to predict one of the outcomes. Which model that you create is the best?
The best score is **BreakPointsOpportunities** feature: 0.8584159345512928

6. Create a few linear regression models that use two features to predict yearly earnings. 
Which set of two features results in the best model?

The pair 'BreakPointsOpportunities' and 'DoubleFaults' features has the higher score: 0.8658453190647725
The weight of each feature:
    BreakPointsOpportunities: 1450.27053414
    DoubleFaults: 944.50422027

7. Create a few linear regression models that use multiple features to predict yearly earnings. Which set of features results in the best model?



Head to the Codecademy forums and share your set of features that resulted in the highest test score for predicting your outcome. What features are most important for being a successful tennis player?

### Solution

8. Great work! Visit our forums to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.
