from __future__ import print_function
import time
import mlflow
from mlflow.entities import Param, Metric, RunTag
from argparse import ArgumentParser


print("MLflow Version: ", mlflow.version.VERSION)
print("Tracking URI: ", mlflow.tracking.get_tracking_uri())

experiment_name = "hello_world"
print("experiment_name: ", experiment_name)
mlflow.set_experiment(experiment_name)

client = mlflow.tracking.MlflowClient()
experiment_id = client.get_experiment_by_name(experiment_name).experiment_id
print("experiment_id: ", experiment_id)

now = int(time.time()+.5)

# run function w/ three parameters alpha, run_origin, log_artifact
def run(alpha, run_origin, log_artifact):

    # create run context for tracking
    with mlflow.start_run(run_name=run_origin) as run:
        # Print info to CLI: run ID, artifact URI, alpha, log_artifact, run_origin
        print("runId: ", run.info.run_id)
        print("artifact_uri: ", mlflow.get_artifact_uri())
        print("alpha: ", alpha)
        print("log_artifact: ", log_artifact)
        print("run_origin: ", run_origin)

        # Log to MLflow server: alpha as parameter, metric of own choice, run_origin and
        # log_artifact as tags
        mlflow.log_param("alpha", alpha)
        mlflow.log_metric("rmse", 0.789)
        mlflow.set_tag("run_origin", run_origin)
        mlflow.set_tag("log_artifact", log_artifact)

        # If log_artifact is True, then create info.txt file and log it
        if log_artifact:
            with open("info.txt", "w") as f:
                f.write("Hi artifact")
            mlflow.log_artifact("info.txt")

        # Use log_batch method of MLflowClient class to log multiple entities at once: Param,
        # Metric, and RunTag of mlflow.entities w/ values of own choice
        params = [Param("p1", "0.1"), Param("p2", "0.2")]
        metrics = [Metric("m1", 0.1, now, 1), Metric("m2", 0.2, now, 2)]
        tags = [RunTag("t1", "hi1"), RunTag("t2", "hi2")]

        client.log_batch(run.info.run_id, metrics, params, tags)

# Main function: outside call with three parameters alpha, run_origin, and log_artifact
if __name__ == "__main__":

    # parse CLI parameters
    parser = ArgumentParser()
    parser.add_argument("--alpha", dest="alpha", help="alpha", default=0.1, type=float)
    parser.add_argument("--run_origin", dest="run_origin", help="run_origin", type=str, default="")
    parser.add_argument("--log_artifact", dest="log_artifact", help="Log artifact", type=str, default="False")
    args = parser.parse_args()

    # call run function to conduct run and store to MLflow
    run(args.alpha, args.run_origin, args.log_artifact=="True")
