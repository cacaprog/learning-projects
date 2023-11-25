
## [Homework](https://github.com/cacaprog/machine-learning-zoomcamp/blob/master/cohorts/2023/06-trees/homework.md#homework)

> Note: sometimes your answer doesn't match one of the options exactly. That's fine. Select the option that's closest to your solution.

### [Dataset](https://github.com/cacaprog/machine-learning-zoomcamp/blob/master/cohorts/2023/06-trees/homework.md#dataset)

In this homework, we will use the California Housing Prices from [Kaggle](https://www.kaggle.com/datasets/camnugent/california-housing-prices).

Here's a wget-able [link](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv):

```shell
wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv
```

The goal of this homework is to create a regression model for predicting housing prices (column `'median_house_value'`).

### Preparing the dataset
For this homework, we only want to use a subset of data. This is the same subset we used in homework #2.

First, keep only the records where `ocean_proximity` is either `'<1H OCEAN'` or `'INLAND'`

Preparation:

- Fill missing values with zeros.
- Apply the log tranform to `median_house_value`.
- Do train/validation/test split with 60%/20%/20% distribution.
- Use the `train_test_split` function and set the `random_state` parameter to 1.
- Use `DictVectorizer(sparse=True)` to turn the dataframe into matrices.

## Question 1

Let's train a decision tree regressor to predict the `median_house_value` variable.

- Train a model with `max_depth=1`.

Which feature is used for splitting the data?

> Nenhuma destas opções apareceu no meu código

- `ocean_proximity`


## Question 2

Train a random forest model with these parameters:

- `n_estimators=10`
- `random_state=1`
- `n_jobs=-1` (optional - to make training faster)

What's the RMSE of this model on validation?

- 0.245


## Question 3

Now let's experiment with the `n_estimators` parameter

- Try different values of this parameter from 10 to 200 with step 10.
- Set `random_state` to `1`.
- Evaluate the model on the validation dataset.

After which value of `n_estimators` does RMSE stop improving?

- 50


## Question 4

Let's select the best `max_depth`:

- Try different values of `max_depth`: `[10, 15, 20, 25]`
- For each of these values, try different values of `n_estimators` from 10 till 200 (with step 10)
- Fix the random seed: `random_state=1`

What's the best `max_depth`:

- 20

# Question 5

We can extract feature importance information from tree-based models.

At each step of the decision tree learning algorith, it finds the best split. When doint it, we can calculate "gain" - the reduction in impurity before and after the split. This gain is quite useful in understanding what are the imporatant features for tree-based models.

In Scikit-Learn, tree-based models contain this information in the [`feature_importances_`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.feature_importances_) field.

For this homework question, we'll find the most important feature:

- Train the model with these parametes:
    - `n_estimators=10`,
    - `max_depth=20`,
    - `random_state=1`,
    - `n_jobs=-1` (optional)
- Get the feature importance information from this model

What's the most important feature?

- `median_income`


## Question 6

Now let's train an XGBoost model! For this question, we'll tune the `eta` parameter:

- Install XGBoost
- Create DMatrix for train and validation
- Create a watchlist
- Train a model with these parameters for 100 rounds:

```
xgb_params = {
    'eta': 0.3, 
    'max_depth': 6,
    'min_child_weight': 1,
    
    'objective': 'reg:squarederror',
    'nthread': 8,
    
    'seed': 1,
    'verbosity': 1,
}
```

Now change `eta` from `0.3` to `0.1`.

Which eta leads to the best RMSE score on the validation dataset?

- 0.3

## [Submit the results](https://github.com/cacaprog/machine-learning-zoomcamp/blob/master/cohorts/2023/06-trees/homework.md#submit-the-results)

- Submit your results here: TBA
- If your answer doesn't match options exactly, select the closest one.
- You can submit your solution multiple times. In this case, only the last submission will be used

## [Deadline](https://github.com/cacaprog/machine-learning-zoomcamp/blob/master/cohorts/2023/06-trees/homework.md#deadline)

The deadline for submitting is October 23 (Monday), 23:00 CET. After that the form will be closed.

