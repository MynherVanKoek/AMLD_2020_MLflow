#!/bin/bash

if [ ! -d "/mlruns" ]; then mkdir /mlruns; fi

/usr/bin/mlflow server \
    --host 0.0.0.0 \
    --default-artifact-root /mlruns \
    --backend-store-uri /mlruns
