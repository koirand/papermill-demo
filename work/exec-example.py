import os
import papermill as pm

pm.execute_notebook(
   f'{os.environ["HOME"]}/work/example.ipynb',
   f'{os.environ["HOME"]}/work/example-output-python.ipynb',
   parameters = dict(a=7, b=9)
)
