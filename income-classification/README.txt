# Dataset

The dataset has been loaded for you in script.py and saved as a DataFrame named df. Some of the input and output features of interest are:

    age: continuous
    workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
    education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool
    race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black
    sex: Female, Male
    capital-gain: continuous
    capital-loss: continuous
    hours-per-week: continuous
    native country: discrete
    income: discrete, >50K, <=50K

# Tasks

EDA and Logistic Regression Assumptions
1. The dataset has been loaded for you in script.py and saved as a dataframe named df. The outcome variable here is income. Check if the dataset is imbalanced.
2. Note that all the predictor variables are all categorical. Transform the dataset of predictor variables to dummy variables and save this in a new DataFrame called df_dummies.
3. Using df_dummies, create a heatmap of the correlation values.
4. Determine is scaling is needed for df_dummies prior to modeling. Create output variable y which is binary, 0 when income is less than $50K, 1 when it is greather than $50K.

Logistic Regression Models and Evaluation
5. Using x_train, x_test, y_train, y_test, fit a logistic regression model in scikit-learn on the training set with parameters C=0.05, penalty='l1', solver='liblinear'.
6. Print the model parameters (intercept and coefficients).
7. Evaluate the predictions of the model on the test set. Print the confusion matrix and accuracy score.
8. Create a new DataFrame of the model coefficients and variable names. Sort values based on coefficient and exclude any that are equal to zero. Print the values of the DataFrame.
9. Create a barplot of the coefficients sorted in ascending order. What are the most important features?
10. Plot the ROC curve and print the AUC value.

