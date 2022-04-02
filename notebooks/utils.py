import gc
from typing import Iterable

import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf


class F1Score(tf.keras.metrics.Metric):
    """
    The tfa.metrics.F1Score (https://www.tensorflow.org/addons/api_docs/python/tfa/metrics/F1Score)
    requires some reshaping that is inconsistent with the other metrics we like to track
    so we will define it from scratch.
    """
    def __init__(self, name="f1_score", **kwargs):
        super().__init__(name=name, **kwargs)
        self.f1 = self.add_weight(name="f1", initializer="zeros")
        self.precision_fn = tf.keras.metrics.Precision()
        self.recall_fn = tf.keras.metrics.Recall()

    def update_state(self, y_true, y_pred, sample_weight=None):
        p = self.precision_fn(y_true, y_pred)
        r = self.recall_fn(y_true, y_pred)
        self.f1.assign(2 * ((p * r) / (p + r + 1e-10)))

    def result(self):
        return self.f1

    def reset_state(self):
        # we also need to reset the state of the precision and recall objects
        self.precision_fn.reset_state()
        self.recall_fn.reset_state()
        self.f1.assign(0)


def study_oriented_transformation(dataset: pd.DataFrame) -> Iterable:
    """
    Transforms a dataset into a study-oriented format, to be able to perform per-study evaluation.
    The dataset is expected to have the following columns:
        * study_path: the path to the study.
        * label: the label of the study (e.g. 1 for positive, 0 for negative).
        * prediction: the model prediction (e.g. a probability).
    """
    for (study_type, study_path), group in dataset.groupby(["study_type", "study_path"]):

        study_label = group["label"].values.take(0)
        study_prediction = 1 if group["prediction"].mean() > 0.5 else 0

        yield study_type, study_path, study_label, study_prediction


def inspect_df(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Helper method to easily inspect DataFrames."""

    print(f"shape: {df.shape}")

    return df.head(n)


def clean_up(model_):
    """A clean up strategy for a tf.keras.Model, to ensure no state is transferred between learning experiments."""
    tf.keras.backend.clear_session()
    del model_
    gc.collect()


def plot_metrics(
    history: tf.keras.callbacks.History,
    metrics: list = ["loss", "cohen_kappa", "precision", "recall"],
) -> None:

    plt.rcParams["figure.figsize"] = (18, 15)

    for n, metric in enumerate(metrics):
        name = metric.replace("_", " ").capitalize()
        plt.subplot(2, 2, n + 1)
        plt.plot(
            history.epoch, history.history[metric], linewidth=1.8, label="training"
        )
        plt.plot(
            history.epoch,
            history.history["val_" + metric],
            linestyle="--",
            linewidth=1.8,
            label="validation",
        )
        plt.xlabel("epoch")
        plt.ylabel(name)
        if metric == "loss":
            plt.ylim([0, plt.ylim()[1]])
        elif metric == "cohen_kappa":
            plt.ylim([-1, 1])
        else:
            plt.ylim([0, 1])

        plt.legend()