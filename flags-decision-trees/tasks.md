## Investigate the data

1. The dataset has been loaded for you in script.py and saved as a dataframe named df. Some of the input and output features of interest are:

    name: Name of the country concerned
    landmass: 1=N.America, 2=S.America, 3=Europe, 4=Africa, 5=Asia, 6=Oceania
    bars: Number of vertical bars in the flag
    stripes: Number of horizontal stripes in the flag
    colours: Number of different colours in the flag
    red: 0 if red absent, 1 if red present in the flag

…

    mainhue: predominant colour in the flag (tie-breaks decided by taking the topmost hue, if that fails then the most central hue, and if that fails the leftmost hue)
    circles: Number of circles in the flag
    crosses: Number of (upright) crosses
    saltires: Number of diagonal crosses
    quarters: Number of quartered sections
    sunstars: Number of sun or star symbols

**We will build a decision tree classifier to predict what continent a particular flag comes from. Before that, we want to understand the distribution of flags by continent. Calcluate the count of flags by landmass value.**

2. Rather than looking at all six continents, we will focus on just two, Europe and Oceania. Create a new dataframe with only flags from Europe and Oceania.

3. Given the list of predictors in the list var, print the average values of each for these two continents. Note which predictors have very different averages.

4. We will build a classifier to distinguish flags for these two continents – but first, inspect the variable types for each of the predictors.

labels = (df["landmass"].isin([3,6]))*1

5. Note that all the predictor variables are numeric except for mainhue. Transform the dataset of predictor variables to dummy variables and save this in a new dataframe called data.

6. Split the data into a train and test set.

## Tune Decision Tree Classifiers by Depth

7. We will explore tuning the decision tree model by testing the performance over a range of max_depth values. Fit a decision tree classifier for max_depth values from 1-20. Save the accuracy score in for each depth in the list acc_depth.

8. Plot the accuracy of the decision tree models versus the max_depth.

9. Find the largest accuracy and the depth this occurs.

10. Refit the decision tree model using the max_depth from above; plot the decision tree.

## Tune Decision Tree Classifiers by Pruning

11. Like we did with max_depth, we will now tune the tree by using the hyperparameter ccp_alpha, which is a pruning parameter. Fit a decision tree classifier for each value in ccp. Save the accuracy score in the list acc_pruned.

12. Plot the accuracy of the decision tree models versus the ccp_alpha.

13. Find the largest accuracy and the ccp_alpha value this occurs.

14. Fit a decision tree model with the values for max_depth and ccp_alpha found above. Plot the final decision tree.

15. Nice work! Note that the accuracy of our final model increased and the structure of the tree was simpler – many unnecessary branches were removed in the pruning process making for a much easier interpretation.

### There are a few different ways to extend this project:

    - Try to classify something else! Rather than predicting the "Landmass" feature, could predict something like the "Language"?
    
    - Find a subset of features that work better than what we’re currently using. An important note is that a feature that has categorical data won’t work very well as a feature. For example, we don’t want a decision node to split nodes based on whether the value for "Language" is above or below 5.
    
    - Tune more parameters of the model. You can find a description of all the parameters you can tune in the Decision Tree Classifier documentation. For example, see what happens if you tune max_leaf_nodes. Think about whether you would be overfitting or underfitting the data based on how many leaf nodes you allow.
