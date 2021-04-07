from datetime import timedelta
from airflow import DAG
from airflow.operators.papermill_operator import PapermillOperator
from airflow.utils.dates import days_ago

dag = DAG(
    'example_papermill_operator',
    schedule_interval=None,
    start_date=days_ago(1),
)

task = PapermillOperator(
    task_id="run_example_notebook",
    input_nb="/tmp/work/example.ipynb",
    output_nb="/tmp/work/output-airflow.ipynb",
    parameters={"a": 1, "b": 2},
    dag=dag,
)
