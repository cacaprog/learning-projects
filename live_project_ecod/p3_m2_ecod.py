import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import numpy as np
import scipy
import sys
from datasets.path import DATASET_PATH

from src.milestone3.p3_m1_ecod import skewness
from src.milestone1.p1_m1_roc_auc import auc_roc

def ecdf(data):
    """
    -------------------------------------------------------------------------------------------------------------------------------
    Args:
        data: Array of feature observations

    Returns:
        Array of ecdf values calculated for each original entry based on all given entries e.g.

        data = [1,2,3,4]
        returns [ecdf(1),ecdf(2),ecdf(3),ecdf(4)]

    -------------------------------------------------------------------------------------------------------------------------------
    """
    sorted_data = np.sort(data)
    val_to_counts = []
    current_value = sorted_data[0]
    count = 0
    for entry in sorted_data:
        if entry == current_value:
            val_to_counts.append((entry, count))
            current_value = entry

        count = count + 1

    val_to_counts.append((entry, count)

    num_entries = float(len(data))
    val_to_counts = {k: v / num_entries for k, v in val_to_counts}

    cumulative_prob = np.array(for entry in data:
                               val_to_counts[entry])

    return cumulative_prob


class ECODScorerV2:
    def __init__(self, data) -> None:
        self.data = data

    def score(self, samples):
        original_size = samples.shape[0]
        num_features = len(self.data[0])
        all_data = np.concatenate((self.data, samples), axis=0)
        skewness_values = np.sign(
            np.array([skewness(all_data[:, i]) for i in range(num_features)]))

        """
        -------------------------------------------------------------------------------------------------------------------------------
        o_left_scores:
        Array of shape (all_data size, num_features)
        Each entry corresponds to the negative log left cumulative probability distribution value for the feature
        i.e.
        [-log(F_left(f1)), -log(F_left(f2)),..., -log(F_left(fd))]
        -------------------------------------------------------------------------------------------------------------------------------
        """
        # create array of shape (all_data size, num_features)
        # Each entry corresponds to the negative log left cumulative probability distribution value for the feature

        o_left_scores = -1 * np.log(np.apply_along_axis(ecdf, 0, all_data))

        """
        o_right_scores:
        Array of shape (all_data size, num_features)
        Each entry corresponds to the negative log  right cumulative probability distribution value for the feature
        i.e.
        [-log(F_right(f1)), -log(F_right(f2)),..., -log(F_right(fd))]
        
        """
        o_right_scores = -1 * np.log(np.apply_along_axis(ecdf, 0, -1 * all_data))

        """
        -------------------------------------------------------------------------------------------------------------------------------
        o_auto_scores:
        Array of shape (all_data size, num_features)
        Each entry corresponds to the negative log of the left ECDF if the feature skewness is negative. Else it should be
        the negative log of the right ECDF
        e.g
        [-log(F_right(f1)), -log(F_left(f2)),...]

        where we assume that the skewness of feature 1 is positive and the skewness of feature 2 is negative
        -------------------------------------------------------------------------------------------------------------------------------
        """
        o_auto_scores = o_left_scores * np.heaviside() + \
            o_right_scores * np.heaviside(<CODE>, 1)

        scores = np.maximum(o_left_scores.sum(
            axis=1), o_right_scores.sum(axis=1))
        scores = np.maximum(o_auto_scores.sum(axis=1), scores)[-original_size:]

        return scores.ravel()


class ECODScorerBug:
    def __init__(self, data) -> None:
        self.data = data

    def score(self, samples):
        original_size = samples.shape[0]
        num_features = len(self.data[0])
        all_data = np.concatenate((self.data, samples), axis=0)
        skewness_values = np.sign(
            np.array([skewness(all_data[:, i]) for i in range(num_features)]))

        o_left_scores = <CODE>

        o_right_scores = <CODE>

        o_auto_scores = <CODE>

        scores = np.maximum(o_left_scores, o_right_scores)
        scores = np.maximum(scores, o_auto_scores).sum(axis=1)[-original_size:]

        return scores.ravel()


if __name__ == '__main__':

    datasets = ["breastw.mat",
                "lympho.mat",
                "mammography.mat",
                # "forestCover.mat", #NOTE: ECODScorerV1 can take a really long time processing this data set
                ]

    if sys.argv[1] == 'performance':

        from sklearn.model_selection import train_test_split
        import time
        from src.milestone3.p3_m1_ecod import ECODScorerV1

        def time_cases(test_case, method):
            dataset = scipy.io.loadmat(DATASET_PATH + "/" + test_case)
            features = dataset['X']
            labels = dataset['y']

            auc_results = []
            time_results = []
            num_samples = len(labels)
            for idx in range(10):
                X_train, X_test, _, y_test = train_test_split(
                    features, labels, test_size=0.40, random_state=23423 + idx)
                try:
                    start = time.perf_counter()
                    fitted = method(X_train)
                    predictions = fitted.score(X_test)
                    end = time.perf_counter()
                    auc = auc_roc(y_test, predictions)
                    auc_results.append(auc)
                    time_results.append(end - start)

                except:
                    pass

            mean_auc_score = np.mean(np.array(auc_results))
            mean_time = np.mean(np.array(time_results))

            print(
                f"[{mean_time:0.5f} s] number of samples: {num_samples}, mean auc:{mean_auc_score:0.5f}, test case: {test_case}")

        """
        Compare implementations performance here
        """
        for dataset in datasets:
            time_cases(dataset, ECODScorerV2)

    elif sys.argv[1] == 'bug':

        from pyod.models.ecod import ECOD

        class PyOdECODWRAPPER:
            def __init__(self, data) -> None:
                self._ecod = ECOD()
                self._ecod.fit(data)

            def score(self, samples):
                return self._ecod.decision_function(samples)

        def test_scoring_pyod(test_case):
            dataset = scipy.io.loadmat(DATASET_PATH + "/" + test_case)
            features = dataset['X']
            labels = dataset['y']

            pyod_scores = PyOdECODWRAPPER(features).score(features)
            pyod_auc = auc_roc(labels, pyod_scores)

            ecod_bug_scores = ECODScorerBug(features).score(features)
            ecod_bug_auc = auc_roc(labels, ecod_bug_scores)

            scores_match = np.abs((pyod_scores - ecod_bug_scores)) <= 1e-14
            scores_match = scores_match.all()

            auc_match = pyod_auc == ecod_bug_auc

            print(f"==== {test_case} ===")
            print(f"All scores match up to 1e-14: {scores_match}")
            print(f"AUC match: {auc_match}")
            print("\n\n")

            pass


        for dataset in datasets:
            test_scoring_pyod(dataset)
