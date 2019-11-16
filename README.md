# Introduction to MLflow: managing the ML lifecycle from experimentation to deployment

## Setup
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
python -m venv sklearn_venv
sklearn_venv\Scripts\activate
pip install mlflow sklearn matplotlib jupyter
python -m ipykernel install --user --name sklearn_venv --display-name "Python (MLflow sklearn)"
deactivate
```
Linux
```bash
python -m venv sklearn_venv
. sklearn_venv/bin/activate
pip install mlflow sklearn matplotlib jupyter
python -m ipykernel install --user --name sklearn_venv --display-name "Python (MLflow sklearn)"
deactivate
```

## Running the MLflow server
### Locally
Windows
```bash
mlflow_server\Scripts\activate
mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri ./mlruns --default-artifact-root ./mlruns
```
Linux
```bash
. mlflow_server/bin/activate
mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri ./mlruns --default-artifact-root ./mlruns
```
The MLflow server is now running on http://localhost:5000, this value needs to be assigned to the environment variable `MLFLOW_TRACKING_URI`.

### With Docker
The folder `docker` provides a `Dockerfile` and a `startup.sh` script that enables you run the MLflow service in a Docker container. In the given script, the artifacts and metadata are stored in a folder in that container, which is certainly not the best approach. For alternatives including cloud storage by common providers, check [MLflow's documentation](https://mlflow.org/docs/latest/tracking.html#mlflow-tracking-servers).
