# Predict Wine Quality with Regularization

The data you’re going to be working with is from the Wine Quality Dataset in the UCI Machine Learning Repository. We’re looking at the red wine data in particular and while the original dataset has a 1-10 rating for each wine, we’ve made it a classification problem with a wine quality of good (>5 rating) or bad (<=5 rating). 

### The goals of this project are to:

1. implement different logistic regression classifiers
2. find the best ridge-regularized classifier using hyperparameter tuning
3. implement a tuned lasso-regularized feature selection method

### What we’re working with:

• 11 input variables (based on physicochemical tests): ‘fixed acidity’, ‘volatile acidity’, ‘citric acid’, ‘residual sugar’,’chlorides’, ‘free sulfur dioxide’, ‘total sulfur dioxide’, ‘density’, ‘pH’, ‘sulphates’ and ‘alcohol’.

• An output variable, ‘quality’ (0 for bad and 1 for good)

## Tasks

**Logistic Regression Classifier without Regularization**
1. Before we begin modeling, let’s scale our data using StandardScaler(). Use StandardScaler().fit() to fit the variable features and then use transform() to get X to get the transformed input to our model.

2. Perform an 80:20 train-test split on the data. Set the random_state to 99 for reproducibility.

3. Define a classifier, clf_no_reg, a logistic regression model without regularization and fit it to the training data.

4. We’re now going to plot the coefficients obtained from fitting the Logistic Regression model. Copy-paste the following code to get the ordered coefficients as a bar plot:

```
predictors = features.columns
coefficients = clf_no_reg.coef_.ravel()
coef = pd.Series(coefficients,predictors).sort_values()
coef.plot(kind='bar', title = 'Coefficients (no regularization)')
plt.tight_layout()
plt.show()
plt.clf()
```

5. You’re now ready to evaluate this classifier! In the case of linear regression, we evaluated our models using mean-squared-error. For classifiers, it is important that the classifier not only has high accuracy, but also high precision and recall, i.e., a low false positive and false negative rate.

A metric known as f1 score, which is the weighted mean of precision and recall, captures the performance of a classifier holistically. It takes values between 0 and 1 and the closer it is to 1, the better the classifier. Use f1_score() to calculate the f1 score for the training and test data.
Logistic Regression with L2 Regularization

6. We’ve seen in the previous article that the default implementation of logistic regression in scikit-learn is ridge-regularized! Use the default implementation to implement a classifier clf_default that is L2-regularized.

7. Obtain the training and test f1_score for the ridge-regularized classifier using code similar to what we have in Task 5. Notice if either score goes up or down.

8. The scores remain the same! Does this mean that regularization did nothing? Indeed! This means that the constraint boundary for the regularization we performed is large enough to hold the original loss function minimum, thus rendering our model the same as the unregularized one.

How can we tune up the regularization? Recall that C is the inverse of the regularization strength (alpha), meaning that smaller values of C correspond to more regularization. The scikit-learn default for C is 1; therefore, in order to increase the amount of regularization, we need to consider values of C that are less than 1. But how far do we need to go? Let’s try a coarse-grained search before performing a fine-grained one.

Define an array, C_array that takes the values C_array = [0.0001, 0.001, 0.01, 0.1, 1]. Get an array each for the training and test scores corresponding to these values of C.

9. Use the following plotting code to plot the training and test scores as a function of C. Does this clarify the range of C’s we need to be doing a fine-grained search for?
```
plt.plot(C_array,training_array)
plt.plot(C_array,test_array)
plt.xscale('log')
plt.show()
plt.clf()
```

**Hyperparameter Tuning for L2 Regularization**

10. We’re now ready to perform hyperparameter tuning using GridSearchCV! Looking at the plot, the optimal C seems to be somewhere around 0.001 so a search window between 0.0001 and 0.01 is not a bad idea here.

Let’s first get setup with the right inputs for this. Use np.logspace() to obtain 100 values between 10^(-4) and 10^(-2) and define a dictionary of C values named tuning_C that can function as an input to GridSearchCV‘s parameter grid.

11. Define a grid search model on the parameter grid defined above for a logistic regression model with ridge regularization. Set the scoring metric to ‘f1’ and the number of folds to 5. Fit this to the training data.

12. Obtain the best C value from this search and the score corresponding to it using the best_params_ and best_score attributes respectively.

13. The score you got above reflects the mean f1-score on the 5 folds corresponding to the best classifier. Notice however that we haven’t yet used the test data, X_test, y_test from our original train-test split! This was done with good reason: the original test data can now be used as our validation dataset to validate whether our “best classifier” is doing as well as we’d like it to on essentially unknown data.

Define a new classifier clf_best_ridge that corresponds to the best C value you obtained in the previous task. Fit it to the training data and obtain the f1_score on the test data to validate the model.
Feature Selection using L1 Regularization

14. We’re now going to use a grid search cross-validation method to regularize the classifier, but with L1 regularization instead. Instead of using GridSearchCV, we’re going to use LogisticRegressionCV. The syntax here is a little different. The arguments to LogisticRegressionCV that are relevant to us:

    Cs : A list/array of C values to check; choose values between 0.01 and 100 here.
    cv : Number of folds (5 is a good choice here!)
    penalty : Remember to choose 'l1' for this!
    solver : Recall that L1 penalty requires that we specify the solver to be ‘liblinear’.
    scoring : 'f1' is still a great choice for a classifier.

Using the above, define a cross-validated classifier, clf_l1 and fit (X,y) here. (Note that we’re not doing a train-test-validation split like last time!)

15. The classifier has the attribute C_ which prints the optimal C value. The attribute coef_ gives us the coefficients of the best lasso-regularized classifier. Print both of these.

16. We can now reproduce the coefficient plot we’d produced for the unregularized scenario. Use the following lines of code to plot the sorted values of the coefficients as a bar plot:

coefficients = clf_l1.coef_.ravel()
coef = pd.Series(coefficients,predictors).sort_values()
 
plt.figure(figsize = (12,8))
coef.plot(kind='bar', title = 'Coefficients for tuned L1')
plt.tight_layout()
plt.show()
plt.clf()

17. Notice how our L1 classifier has set one of the coefficients to zero! We’ve effectively eliminated one feature, density, from the model, thus using Lasso regularization as a feature selection method here.
