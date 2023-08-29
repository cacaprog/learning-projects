import numpy as np
from scipy import stats
import scipy.io as sio

# load shuttle.mat file
data = sio.loadmat('shuttle.mat')
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
    z = sample[feature_idx]
    n = len(data)
    result = 0.0
    for entry in data:
        if predicate(entry[feature_idx], z):
            result += 1

    return result / n


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
    return tail(sample, data, feature_idx, lambda x, y: x <= y)


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
    return tail(sample, data, feature_idx, lambda x, y: x >= y)


def skewness(data):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        data: context data

    Returns:
        Skewness of data

    -------------------------------------------------------------------------------------------------------------------------------
    """
    n = len(data)
    m3 = stats.moment(data, 3)
    m2 = stats.moment(data, 2)
    return n * m3 / ((n - 1) * (n - 2) * m2 ** 1.5)


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

   for feature_idx in range(len(sample)):
       result += np.log(tail_function(sample, data, feature_idx))

   return result


def left_score(sample, data):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        sample: array of float that describe a single observation
        data: context data

    Returns:
         left one sided anomaly score of sample

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
         right one sided anomaly score of sample

    -------------------------------------------------------------------------------------------------------------------------------
    """
    return tail_score(sample, data, right_tail)


def auto_score(sample, data):
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
        if skewness[feature_idx] >= 0:
            result += np.log(left_tail(sample, data, feature_idx))
        else:
            result += np.log(right_tail(sample, data, feature_idx))

    return result


class ECODScorev1:
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Implements the ECOD  anomaly detection algorithm

    Atributes:
        data: training data
    --------------------------------------------------------------------------------------------------------------------------------   
    """
    
    def __init__(self, data):
        num_features = len(data[0])
        self.num_features = num_features
        self.data = data
    
    def score_single(self, sample, data, skewness):
        """
        -------------------------------------------------------------------------------------------------------------------------------
        Args:
            sample: array of float that describe a single observation
            data: context data and 

        Returns:
             ECOD anomaly score of sample.

        -------------------------------------------------------------------------------------------------------------------------------
        """


        o_left_score = left_score(sample, data)
        o_right_score = right_score(sample, data)
        o_auto_score = auto_score(sample, data)

        return np.max([o_left_score, o_right_score, o_auto_score])
    
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
        data_swewness = np.array([skewness(all_data[:, i]) for i in range(self.num_features)])
        return np.array([self.score_single(sample, all_data, data_swewness) for sample in data])
    

