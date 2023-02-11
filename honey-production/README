# Honey Production

Now that you have learned how linear regression works, let’s try it on an example of real-world data.

As you may have already heard, the honeybees are in a precarious state right now. You may have seen articles about the decline of the honeybee population for various reasons. You want to investigate this decline and how the trends of the past predict the future for the honeybees.

## Data
Columns:
- state	
- numcol
- yieldpercol
- totalprod
- stocks
- priceperlb
- prodvalue
- year

## Check out the data
1. Load tha data

2. For now, we care about the total production of honey per year. Use the .groupby() method provided by pandas to get the mean of totalprod per year.

Store this in a variable called prod_per_year.

3. Create a variable called X that is the column of years in this prod_per_year DataFrame.

After creating X, reshape it

4. Create a variable called y that is the totalprod column in the prod_per_year dataset.

5. Plot y vs X as a scatterplot.


## Create and Fit a Linear Regression Model
6. Create a linear regression model from scikit-learn and call it regr

7. Fit the model to the data

8. After you have fit the model, print out the slope of the line (stored in a list called regr.coef_) and the intercept of the line (regr.intercept_)

slope: -88303.18915238195
intercept: 181208083.10732982

9. Create a list called y_predict that is the predictions your regr model would make on the X data

10. Plot y_predict vs X as a line

## Predict the Honey decline
11. So, it looks like the production of honey has been in decline, according to this linear model. Let’s predict what the year 2050 may look like in terms of honey production.

a. Our known dataset stops at the year 2013, so let’s create a NumPy array called X_future that is the range from 2013 to 2050

b. After creating that array, we need to reshape it for scikit-learn

reshape() is a little tricky! It might help to print out X_future before and after reshaping

12. Create a list called future_predict that is the y-values that your regr model would predict for the values of X_future

13. Plot future_predict vs X_future on a different plot.

How much honey will be produced in the year 2050, according to this?




