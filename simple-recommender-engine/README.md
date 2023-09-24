## What is Surprise?

Surprise (an abbreviation of _Simple Python Recommendation System Engine_) is a `scikit`, a software library built as an add-on to the numerical computation library `SciPy`. Much like how `scikit-learn` makes developing and testing different machine learning models easy, Surprise makes developing and testing various recommender system algorithms easy. Surprise comes with several modules that make it easy to transform data, train recommender systems, and measure recommender system performance. It also comes with a solid base of documentation that makes it easy to understand and explore the library’s capabilities.

## Building A Simple Recommender System

We’re now going to use Surprise to build a basic recommender system. We will be using a classic dataset, the [MovieLens Dataset](https://grouplens.org/datasets/movielens/), to build a recommender system that suggests movies to users based on the ratings they gave several movies. The MovieLens dataset is a set of 100,000 movie ratings for 9,000 movies provided by 600 users. The ratings come from the website [movielens.org](https://movielens.org/), a non-commercial site dedicated to giving users personalized movie recommendations. This data is very similar to the type of data you would find at large commercial streaming services.

