# Introduction to MLflow: managing the ML lifecycle from experimentation to deployment
Developing adequate machine learning models involves a lot of experimentation where different models or tools are tested, modified, discarded or eventually accepted. During this process, however, any history or traceable development that lead to the latest model may get lost since models usually are not being versioned continuously and their performance is not being stored. Results may then no longer be reproducible.

In this workshop, we will introduce MLflow and show how you can integrate this model management framework into the ML lifecycle, from tracking experiments to eventually deploying models.

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

## Disclaimer
Most of the documentation in this Git Repository is directly taken from [MLlfow's website](https://www.mlflow.org/docs/latest/index.html). It is condensed to explain the functionalities that I think are most important to be discussed in an introductory workshop. For more information and a deeper insight, please directly consult MLflow's documentation.

At the time of writing, the latest version was v1.5.0, which was used to prepare and conduct this workshop.

## Overview on MLflow
MLflow is an open source platform for managing the end-to-end machine learning lifecycle. It tackles three primary functions:
* Tracking experiments to record and compare parameters and results
* Packaging ML code in a reusable, reproducible form in order to share with other data
  scientists or transfer to production
* Managing and deploying models from a variety of ML libraries to a variety of model serving and
  inference platforms

MLflow is library-agnostic. It can be used with any machine learning library, and in any programming language, since all functions are accessible through a REST API and CLI. For convenience, the project also includes a Python API, R API, and Java API. Here, we only concentrate on the Python API.

In this workshop, we will discuss MLflow's three components: [MLflow Tracking](./10_tracking/tracking.md), [MLflow Projects](./20_projects/projects.md), and [MLflow Models](./30_models/models.md).