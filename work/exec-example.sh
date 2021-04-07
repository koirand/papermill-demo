#!/bin/bash

pip install papermill
papermill \
    ${HOME}/work/example.ipynb \
    ${HOME}/work/output-cli.ipynb \
    -p a 5 \
    -p b 7
