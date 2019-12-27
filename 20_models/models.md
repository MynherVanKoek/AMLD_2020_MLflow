# MLflow Models Python API
So far, we have learnt how to integrate MLflow's tracking functionalities into our model code. Doing
so, we can now trace different runs done with different parameters and their respective outcomes to
better evaluate, compare, discard, or accept a model. However, the model itself has not been stored
yet, which makes it difficult to reproduce results on different machines.

Here, MLflow Models come in handy. They allow you to package machine learning models that can be
used later on. At first, an [overview](#overview) taken from
[MLflow's documentation](https://www.mlflow.org/docs/latest/models.html) is given. Then, we will
integrate these new functions in in our code (see [Tasks](#tasks)).

## Overview
### Storage Format
Each MLflow Model is a directory containing arbitrary files, together with an `MLmodel` file in the
root of the directory that can define multiple flavors that the model can be viewed in.

*Flavors* are a convention that deployment tools can use to understand the model, which makes it
possible to write tools that work with models from any ML library without having to integrate each
tool with each library. MLflow defines several "standard" flavors that all of its built-in
deployment tools support, such as a "Python function" flavor that describes how to run the model as
a Python function. However, libraries can also define and use other flavors. For example, MLflow’s
`mlflow.sklearn` library allows loading models back as a scikit-learn `Pipeline` object for use in
code that is aware of scikit-learn, or as a generic Python function for use in tools that just need
to apply the model (e.g., the `mlflow sagemaker` tool for deploying models to Amazon SageMaker).

All of the flavors that a particular model supports are defined in its `MLmodel` file in YAML
format. For example, `mlflow.sklearn` outputs models as follows:
```bash
# Directory written by mlflow.sklearn.save_model(model, "my_model")
my_model/
├── MLmodel
└── model.pkl
```
And its `MLmodel` file describes two flavors:
```yaml
time_created: 2018-05-25T17:28:53.35

flavors:
  sklearn:
    sklearn_version: 0.19.1
    pickled_model: model.pkl
  python_function:
    loader_module: mlflow.sklearn
```
This model can then be used with any tool that supports either the `sklearn` or `python_function`
model flavor. For example, the `mlflow models serve` command can serve a model with the `sklearn`
flavor:
```bash
mlflow models serve my_model
```
In addition, the `mlflow sagemaker` command-line tool can package and deploy models to AWS SageMaker
as long as they support the `python_function` flavor:
```bash
mlflow sagemaker deploy -m my_model [other options]
```

###  Fields in the MLmodel Format
Apart from a `flavors` field listing the model flavors, the `MLmodel` YAML format can contain the
following fields:
* `time_created`: Date and time when the model was created, in UTC ISO 8601 format.
* `run_id`: ID of the run that created the model, if the model was saved using `tracking`.

###  Model API

You can save and load MLflow Models in multiple ways. First, MLflow includes integrations with
several common libraries. For example, :py:mod:`mlflow.sklearn` contains
:py:func:`save_model <mlflow.sklearn.save_model>`, :py:func:`log_model <mlflow.sklearn.log_model>`,
and :py:func:`load_model <mlflow.sklearn.load_model>` functions for scikit-learn models. Second,
you can use the :py:class:`mlflow.models.Model` class to create and write models. This
class has four key functions:

* :py:func:`add_flavor <mlflow.models.Model.add_flavor>` to add a flavor to the model. Each flavor
  has a string name and a dictionary of key-value attributes, where the values can be any object
  that can be serialized to YAML.
* :py:func:`save <mlflow.models.Model.save>` to save the model to a local directory.
* :py:func:`log <mlflow.models.Model.log>` to log the model as an artifact in the
  current run using MLflow Tracking.
* :py:func:`load <mlflow.models.Model.load>` to load a model from a local directory or
  from an artifact in a previous run.

Built-In Model Flavors
----------------------

MLflow provides several standard flavors that might be useful in your applications. Specifically,
many of its deployment tools support these flavors, so you can export your own model in one of these
flavors to benefit from all these tools:


## Tasks