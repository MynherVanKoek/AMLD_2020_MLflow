# Introduction to MLflow: managing the ML lifecycle from experimentation to deployment

## Prerequisites
* To run code and set up environments: Python 3
* To run MLflow Projects and MLflow Models:
  * Get conda >= 4.6
  * Additionally, configure CLI to activate conda environments. To do so, type `conda init <CLI>` in
    your CLI, where `<CLI>` is `cmd.exe` for Windows users or `bash` for Linux users.

## Setup
For this workshop, we will need some virtual environments:
* one for setting up the server
* one for running `sklearn` examples

The commands to create these environments are given as follows.

### Virtual environment for MLflow server
Windows
```bash
python -m venv mlflow_server
mlflow_server\Scripts\activate
pip install mlflow
deactivate
```
Linux
```bash
python -m venv mlflow_server
. mlflow_server/bin/activate
pip install mlflow
deactivate
```

### Virtual environment with required packages for workshop 
Windows
```bash
python -m venv mlflow_sklearn
mlflow_sklearn\Scripts\activate
pip install mlflow sklearn matplotlib jupyter
python -m ipykernel install --user --name mlflow_sklearn --display-name "Python (MLflow sklearn)"
deactivate
```
Linux
```bash
python -m venv mlflow_sklearn
. mlflow_sklearn/bin/activate
pip install mlflow sklearn matplotlib jupyter
python -m ipykernel install --user --name mlflow_sklearn --display-name "Python (MLflow sklearn)"
deactivate
```

## Running the MLflow server
### Locally
Windows
```bash
mlflow_server\Scripts\activate
mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri file:///%cd%\mlruns --default-artifact-root file:/%cd%\mlruns
```
Linux
```bash
. mlflow_server/bin/activate
mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri file:///$pwd/mlruns --default-artifact-root file:/$pwd/mlruns
```
The MLflow server is now running on <http://localhost:5000>, this value needs to be assigned to the
environment variable `MLFLOW_TRACKING_URI`.

### With Docker
The folder `docker` provides a `Dockerfile` and a `startup.sh` script that enables you run the
MLflow service in a Docker container. In the given script, the artifacts and metadata are stored in
a folder in that container, which is certainly not the best approach. For alternatives including
cloud storage by common providers, check
[MLflow's documentation](https://mlflow.org/docs/latest/tracking.html#mlflow-tracking-servers).