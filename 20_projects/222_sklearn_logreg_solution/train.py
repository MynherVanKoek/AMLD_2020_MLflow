from __future__ import print_function

from argparse import ArgumentParser
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (precision_score, recall_score, f1_score, plot_confusion_matrix,
                             plot_roc_curve)
import matplotlib.pyplot as plt

import mlflow


print("MLflow Version: ", mlflow.version.VERSION)
# mlflow.set_tracking_uri("http://localhost:5000")
print("Tracking URI: ", mlflow.tracking.get_tracking_uri())

experiment_name = "sklearn_logistic_regression"
print("experiment_name: ", experiment_name)
mlflow.set_experiment(experiment_name)

client = mlflow.tracking.MlflowClient()
experiment_id = client.get_experiment_by_name(experiment_name).experiment_id
print("experiment_id: ", experiment_id)

np.random.seed(137)
X, y = datasets.make_classification(n_samples=1000,
                                    n_features=2,
                                    n_informative=2,
                                    n_redundant=0,
                                    n_repeated=0,
                                    n_classes=2)


def run(X, y, penalty='l2', run_origin='localRun'):
    solver = "saga"
    if penalty is "elasticnet":
        l1_ratio = 0.5
    else:
        l1_ratio = None

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    with mlflow.start_run(run_name=run_origin) as run:
        lr = LogisticRegression(penalty=penalty, solver=solver, l1_ratio=l1_ratio)
        lr.fit(X_train, y_train)
        score_train = lr.score(X_train, y_train)
        score_test = lr.score(X_test, y_test)

        prec_test = precision_score(y_test, lr.predict(X_test))
        rec_test = recall_score(y_test, lr.predict(X_test))
        f1_test = f1_score(y_test, lr.predict(X_test))

        print("hyperparameters: ", lr.get_params())
        print("train score: ", score_train)
        print("test score: ", score_test)
        print("test precision: ", prec_test)
        print("test recall: ", rec_test)
        print("test f1 score: ", f1_test)

        disp = plot_confusion_matrix(lr, X_test, y_test)
        print(disp.confusion_matrix)
        plt.savefig("sklearn_logreg_conf_mat.png")

        disp = plot_roc_curve(lr, X_test, y_test)
        plt.savefig("sklearn_logreg_roc_curve.png")

        print("runId: ", run.info.run_id)
        print("artifact_uri: ", mlflow.get_artifact_uri())
        mlflow.log_metrics({"training score": score_train, "test score": score_test})
        mlflow.log_params(lr.get_params())
        mlflow.set_tags({"run_origin": run_origin})
        mlflow.log_artifact("sklearn_logreg_conf_mat.png", "figures")
        mlflow.log_artifact("sklearn_logreg_roc_curve.png", "figures")

if __name__=='__main__':

    # parse CLI parameters
    parser = ArgumentParser()
    parser.add_argument("--penalty", dest="penalty", help="penalty", default="l2", type=str)
    parser.add_argument("--run_origin", dest="run_origin", help="run_origin", type=str, default="")
    args = parser.parse_args()

    # call run function to conduct run and store to MLflow
    run(X, y, args.penalty, args.run_origin)
