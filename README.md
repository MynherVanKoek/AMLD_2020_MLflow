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
pip install mlflow sklearn jupyter
python -m ipykernel install --user --name sklearn_venv --display-name "Python (MLflow sklearn)"
deactivate
```
Linux
```bash
python -m venv sklearn_venv
. sklearn_venv/bin/activate
pip install mlflow sklearn jupyter
python -m ipykernel install --user --name sklearn_venv --display-name "Python (MLflow sklearn)"
deactivate
```

