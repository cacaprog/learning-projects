import numpy as np
from scipy import stats

# load shuttle.mat file on F:\Downloads\
data = np.load('F:\Downloads\shuttle.mat')
print(data)


def tail(sample, data, feature_idx, predicate):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        sample: observation vector, each entry corresponds to a different feature
        data: context data
        feature_idx: index that specifies the feature to be analyzed
        predicate: lambda function of type (float, float) => boolean

    Returns:
        Empirical probability that feature_idx of sample satisfies predicate

    -------------------------------------------------------------------------------------------------------------------------------
    """
    z = # value of the ith sample feature 
    n = # number of observations 
    result = 0.0
    for entry in <CODE>:
        if <CODE>:
            result += 1

    return <CODE>


def left_tail(sample, data, feature_idx):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        sample: observation vector, each entry corresponds to a different feature
        data: context data
        feature_idx: index that specifies the feature to be analyzed

    Returns:
        Empirical probability that the value of feature_idx of a randomly chosen
        observation in data is smaller or equal than the value of feature_idx of sample

    -------------------------------------------------------------------------------------------------------------------------------
    """
    return tail(sample, data, feature_idx, <CODE>)


def right_tail(sample, data, feature_idx):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        sample: observation vector, each entry corresponds to a different feature
        data: context data
        feature_idx: index that specifies the feature to be analyzed

    Returns:
        Empirical probability that the value of feature_idx of a randomly chosen
        observation in data is larger or equal than the value of feature_idx of sample

    -------------------------------------------------------------------------------------------------------------------------------
    """
    return tail(sample, data, feature_idx, <CODE>)


def skewness(data):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        data: array of floats

    Returns:
        Empirical skewness of the data

    -------------------------------------------------------------------------------------------------------------------------------
    """
    n = len(data)
    m3 = stats.moment(data, 3)
    m2 = <CODE> stats.moment(data, 2)
    return <CODE>


def tail_score(sample, data, tail_function):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        sample: array of float that describe a single observation
        data: context data
        tail_function: function to calculate the lef/right empirical cumulative distributions

    Returns:
         one sided anomaly score of sample

    -------------------------------------------------------------------------------------------------------------------------------
    """

    result = 0.0

    for feature_idx in <CODE>:
        result += np.log(<CODE>)

    return -result


def left_score(sample, data):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        sample: array of float that describe a single observation
        data: context data

    Returns:
         left sided anomaly score of sample

    -------------------------------------------------------------------------------------------------------------------------------
    """
    return tail_score(sample, data, left_tail)


def right_score(sample, data):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        sample: array of float that describe a single observation
        data: context data

    Returns:
         right sided anomaly score of sample

    -------------------------------------------------------------------------------------------------------------------------------
    """
    return tail_score(sample, data, right_tail)


def auto_score(sample, data, skewness):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        sample: array of float that describe a single observation
        data: context data
        skewness: array of float where skewness[idx] is the skewness of the idx feature

    Returns:
         Anomaly score based on the feature skewness.

    -------------------------------------------------------------------------------------------------------------------------------
    """
    num_features = len(sample)

    result = 0.0

    for feature_idx in range(num_features):
        if <CODE>:
            result += np.log(<CODE>)
        else:
            result += np.log(<CODE>)

    return -result


class ECODScorerV1:
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Implements the ECOD  anomaly detection algorithm

    Atributes:
        data: training data
    --------------------------------------------------------------------------------------------------------------------------------   
    """

    def __init__(self, data) -> None:
        num_features = len(data[0])
        self.num_features = num_features
        self.data = data

    def _score_single(self, sample, data, skewness):
        """
        -------------------------------------------------------------------------------------------------------------------------------
        Args:
            sample: array of float that describe a single observation
            data: context data and 

        Returns:
             ECOD anomaly score of sample.

        -------------------------------------------------------------------------------------------------------------------------------
        """

        o_left_score = <CODE>
        o_right_score = <CODE>
        o_auto_score = <CODE>

        return <CODE>

    def score(self, data):
        """
        -------------------------------------------------------------------------------------------------------------------------------
        Args:
            data: array of observations that describes the data to be analyzed

        Returns:
             ECOD anomaly scores for each observation in data

        -------------------------------------------------------------------------------------------------------------------------------
        """
        all_data = np.concatenate((self.data, data), axis=0)
        data_skewness = np.array([skewness(all_data[:, i])
                                 for i in range(self.num_features)])
        return np.array([self._score_single(sample, all_data, data_skewness) for sample in data])
