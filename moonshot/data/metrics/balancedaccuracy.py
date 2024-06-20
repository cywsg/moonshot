import logging
import re
import string
from typing import Any

from nltk.stem.porter import *
from sklearn.metrics import balanced_accuracy_score

from moonshot.src.utils.timeit import timeit

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def normalize(text: str, stem: bool) -> str:
    """
    Normalizes strings.

    Args:
        - text: text to normalize
        - stem: whether or not to apply a stemmer

    Returns: normalized text
    """

    # Remove punctuation
    text = str(text).translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = text.strip()

    # Make lower case
    text = text.lower()

    # Stem
    if stem:
        text = PorterStemmer().stem(text)
    return text


class BalancedAccuracy:
    """
    BalancedAccuracy will compare the output from language model with the expected target.
    The balanced accuracy in binary and multiclass classification problems to deal with imbalanced datasets.
    It is defined as the average of recall obtained on each class.
    """

    @staticmethod
    @timeit
    def get_results(
        prompts: Any, predicted_results: Any, targets: Any, *args, **kwargs
    ) -> dict:
        """
        Calculates the balanced accuracy of the predicted results by comparing them to the target results.

        Args:
            prompts (Any): The prompts used for prediction.
            predicted_results (Any): The predicted results.
            targets (Any): The target results.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing the balanced accuracy of the predicted results.
        """
        # Normalize strings before comparing
        normalized_answers = [normalize(a, stem=False) for a in targets]
        normalized_gens = [normalize(g, stem=False) for g in predicted_results]

        # Compute balanced accuracy
        bal_acc = balanced_accuracy_score(normalized_answers, normalized_gens)

        return {"balanced_accuracy": bal_acc}

        # correct = 0
        # total = len(predicted_results)

        # for idx, (result, target) in enumerate(zip(predicted_results, targets)):
        #     if result == target:
        #         correct += 1

        # return {"balanced_accuracy": float(correct / total)}
