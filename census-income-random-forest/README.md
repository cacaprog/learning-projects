# Random Forests Project

In this project, we will be using a dataset containing census information from UCI’s Machine Learning Repository.

By using this census data with a random forest, we will try to predict whether or not a person makes more than $50,000.

Let’s get started!

## Datasets

The original data set is available at the UCI Machine Learning Repository:

    https://archive.ics.uci.edu/ml/datasets/census+income

The dataset has been loaded for you in script.py and saved as a dataframe named df. Some of the input and output features of interest are:

    - age: continuous
    - workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
    - education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool
    - race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black
    - sex: Female, Male
    - capital-gain: continuous
    - capital-loss: continuous
    - hours-per-week: continuous
    - native country: discrete
    - income: discrete, >50K, <=50K

## Tasks

### Investigate the data

1. We will build a random forest classifier to predict the income category. First, take a look at the distribution of income values – what percentage of samples have incomes less than 50k and greater than 50k?

2. There’s a small problem with our data that is a little hard to catch — every string has an extra space at the start. For example, the first row’s native-country is “ United-States”, but we want it to be “United-States”. One way to fix this is to select all columns of type object and use the string method .str.strip().

3. Create a features dataframe X. This should include only features in the list feature_cols and convert categorical features to dummy variables using pd.get_dummies(). Include the paramter drop_first=True to eliminate redundant features.

4. Create the output variable y, which is binary. It should be 0 when income is less than 50k and 1 when it is greater than 50k.

5. Split the data into a train and test set with a test size of 20%.

### Build and Tune Random Forest Classifiers by Depth

6. Instantiate an instance of a RandomForestClassifier() (with default parameters). Fit the model on the train data and print the score (accuracy) on the test data. This will act as a baseline to compare other model performances.

7. We will explore tuning the random forest classifier model by testing the performance over a range of max_depth values. Fit a random forest classifier for max_depth values from 1-25. Save the accuracy score for the train and test sets in the lists accuracy_train, accuracy_test.

8. Find the largest accuracy and the depth this occurs on the test data.

9. Plot the training and test accuracy of the models versus the max_depth.

10. Refit the random forest model using the max_depth from above; save the feature importances in a dataframe. Sort the results and print the top five features.

### Create Additional Features and Re-Tune

11. Looking at the education feature, there are 16 unique values – from preschool to professional school. Rather than adding dummy variables for each value, it makes sense to bin some of these values together. While there are many ways to do this, we will take the approach of combining the values into 3 groups: High school and less, College to Bachelors and Masters and more. Create a new column in df for this new features called education_bin.

12. Like we did previously, we will now add this new feature into our feature list and recreate X.

13. As we did before, we will tune the random forest classifier model by testing the performance over a range of max_depth values. Fit a random forest classifier for max_depth values from 1-25. Save the accuracy score for the train and test sets in the lists accuracy_train, accuracy_test.

14. Find the largest accuracy and the depth this occurs on the test data. Compare the results from the previous model tuned.

15. Plot the training and test accuracy of the models versus the max_depth. Compare the results from the previous model tuned.

16. Refit the random forest model using the max_depth from above; save the feature importances in a dataframe. Sort the results and print the top five features. Compare the results from the previous model tuned.

17. Nice work! Note that the accuracy of our final model increased and one of our added features is now in the top 5 based on importance!

There are a few different ways to extend this project:

    Are there other features that may lead to an even better performace? Consider creating new ones or adding additional features not part of the original feature list.
    Consider tuning hyperparameters based on a different evaluation metric – our classes are fairly imbalanced, AUC of F1 may lead to a different result
    Tune more parameters of the model. You can find a description of all the parameters you can tune in the Random Forest Classifier documentation. For example, see what happens if you tune max_features or n_estimators.

