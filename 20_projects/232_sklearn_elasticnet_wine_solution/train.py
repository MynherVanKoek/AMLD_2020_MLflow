# The data set used in this example is from http://archive.ics.uci.edu/ml/datasets/Wine+Quality
# P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
# Modeling wine preferences by data mining from physicochemical properties. In Decision Support
# Systems, Elsevier, 47(4):547-553, 2009.

from __future__ import print_function

from argparse import ArgumentParser
import os
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

import mlflow
import mlflow.sklearn

import logging


logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

print("MLflow Version: ", mlflow.version.VERSION)
# mlflow.set_tracking_uri("http://localhost:5000")
print("Tracking URI: ", mlflow.tracking.get_tracking_uri())

experiment_name = "sklearn_elasticnet_wine"
print("experiment_name: ", experiment_name)
mlflow.set_experiment(experiment_name)

client = mlflow.tracking.MlflowClient()
experiment_id = client.get_experiment_by_name(experiment_name).experiment_id
print("experiment_id: ", experiment_id)


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def run(data, in_alpha, in_l1_ratio, run_origin="localRun"):

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    # Set default values if no alpha is provided
    if float(in_alpha) is None:
        alpha = 0.5
    else:
        alpha = float(in_alpha)

    # Set default values if no l1_ratio is provided
    if float(in_l1_ratio) is None:
        l1_ratio = 0.5
    else:
        l1_ratio = float(in_l1_ratio)

    # Useful for multiple runs (only doing one run in this sample notebook)
    with mlflow.start_run(run_name=run_origin) as run:

        # Execute ElasticNet
        lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        # Evaluate Metrics
        predicted_qualities = lr.predict(test_x)
        (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

        # Print out metrics
        print("runId: ", run.info.run_id)
        print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)
        print("  hyperparameters: ", lr.get_params())

        # Log parameter, metrics, and model to MLflow
        mlflow.log_params(lr.get_params())
        mlflow.log_metrics({
            "rmse": rmse,
            "r2": r2,
            "mae": mae
        })
        mlflow.set_tags({"run_origin": run_origin})


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the wine-quality csv file from the URL
    csv_url = \
        'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
    try:
        data = pd.read_csv(csv_url, sep=';')
    except Exception as e:
        logger.exception(
            "Unable to download training & test CSV, check your internet connection. Error: %s", e)

    # parse CLI parameters
    parser = ArgumentParser()
    parser.add_argument("--alpha", dest="alpha", help="alpha", default=0.5, type=float)
    parser.add_argument("--l1_ratio", dest="l1_ratio", help="l1 ratio", default=0.5, type=float)
    parser.add_argument("--run_origin", dest="run_origin", help="run_origin", type=str, default="")
    args = parser.parse_args()

    # call run function to conduct run and store to MLflow
    run(data, args.alpha, args.l1_ratio, args.run_origin)
