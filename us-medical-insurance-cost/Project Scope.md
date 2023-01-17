# Project Scope

## Goals
Insurance cost are more expensive for women or men?

What's the mean of cost per region for smokers and no smokers?

How many people are obese (%)?

Healthy people (BMI between 18.5 and 24.9, no smokers) with children pay more than unhealthy people without children?

What features are the most influential for an individual’s medical insurance charges?


## Analysis



## Data
7 columns
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   age       1338 non-null   int64  
 1   sex       1338 non-null   object 
 2   bmi       1338 non-null   float64
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object 
 5   region    1338 non-null   object 
 6   charges   1338 non-null   float64

quantitative: age, bmi, children, charges
categorical: sex, smoker, region

### BMI ranges
For most adults, an ideal BMI is in the 18.5 to 24.9 range.

For children and young people aged 2 to 18, the BMI calculation takes into account age and gender as well as height and weight.

If your BMI is:
- below 18.5 – you're in the underweight range
- between 18.5 and 24.9 – you're in the healthy weight range
- between 25 and 29.9 – you're in the overweight range
- 30 or over – you're in the obese range




## Evaluation


## Output




### Project Extensions

You’re welcome to expand your analysis beyond what you have already done! Some potential extra features to add to your portfolio project are the following:

- Organize your findings into dictionaries, lists, or another convenient datatype.
- Make predictions about what features are the most influential for an individual’s medical insurance charges based on your analysis.
- Explore areas where the data may include bias and how that would impact potential use cases.
