# Biodiversity project

# Introduction

This goal of this project is to analyze biodiversity data from the National Parks Service, particularly around various species observed in different national park locations.

This project will scope, analyze, prepare, plot data, and seek to explain the findings from the analysis.


**Data sources:**

Both `Observations.csv` and `Species_info.csv` was provided by [Codecademy.com](https://www.codecademy.com).

Note: The data for this project is *inspired* by real data, but is mostly fictional.


# Scoping


### Goals
Throught the data provided, I will answer the follow questions:

- What is the distribution of conservation status for species?
- Are certain types of species more likely to be endangered?
- Are the differences between species and their conservation status significant?
- Which animal is most prevalent and what is their distribution amongst parks?

### Data

#### species_info.csv:
**Total:** 5824 rows

**category** - class of species
7 categories: 'Mammal, Bird, Reptile, Amphibian, Fish, Vascular Plant, Nonvascular Plant

**scientific_name** - the scientific name of each species
Total: 5824
Unique: 5541
Two species don't have the same scientific name. Maybe, are duplicated data here. 

**common_name** - the common names of each species
Total: 5824
Unique: 5504
Two species could have a commom name.

**conservation_status** - each species current conservation status
Total: 191
Unique: 4
Endangered, In Recovery, Species of Concern, Threatened
The data collection for conservation status was not concluded. Maybe the team is still working on it, and some especies go throught one status to another (for example: from 'species of concern' to 'In Recovery').

#### observations.csv:
**scientific_name** - the scientific name of each species
Total: 23296
Unique: 5541
This is a column in common in two csv files.
The total here (23296) is 4x the total on species_info.csv (5824)
The unique data is the same observed on species_info.csv

**park_name** - Park where species were found
Total: 23296
Unique: 4
Yellowstone National Park, Yosemite National Park, Bryce National Park, Great Smoky Mountains National Park

**observations** - the number of times each species was observed at park
Total: 23296
The same species could be observed in different parks

### Analysis

In this section, descriptive statistics and data visualization techniques will be employed to understand the data better. Statistical inference will also be used to test if the observed values are statistically significant. Some of the key metrics that will be computed include: 

1. Distributions
1. counts
1. relationship between species
1. conservation status of species
1. observations of species in parks. 

### Evaluation
The lack of conservation_status for hugh number os species is a problem.


# Findings

### What is the distribution of conservation status for animals?

Despite the lack of information for all species, we could observe:
- 86% of animals  have not intervention
- 10% of animals are species of concern
- 1% are endangered
- Less than 1% are threatened
- Less than 1% are in recovery

### Are certain types of species more likely to be endangered?

Our observation, shows that mammals, bird and fish are the top 3 species in danger situation.
According the data:
- 40% mammal
- 26% bird
- 20% fish
- 6% Plant
- 6% Anphibian

Two of all species observed are not in danger: reptile and nonvascular plants.

### Are the differences between species and their conservation status significant?

Mammals and Bird have the most % of protected species in dataset (17% and 15% respectly) but those two variables are independent.

Mammals and Reptiles have a significant relationship.

### Which specie is most prevalent and what is their distribution amongst parks?

Bat are the most prevalent specie in dataset.

Park    Observations
Yellowstone National Park: 4584
Yosemite National Park:	2657
Bryce National Park: 1811
Great Smoky Mountains National Park: 1355

