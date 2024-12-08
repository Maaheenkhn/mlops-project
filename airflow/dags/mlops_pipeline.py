from airflow import DAG
from airflow.operators.bash import BashOperator
# from airflow import BashOperator
from datetime import datetime

with DAG(
    dag_id='mlops_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    preprocess = BashOperator(
        task_id='preprocess',
        bash_command='python /opt/airflow/dags/preprocess.py',
    )

    train = BashOperator(
        task_id='train',
        bash_command='python /opt/airflow/dags/training_script.py',
    )

    preprocess >> train