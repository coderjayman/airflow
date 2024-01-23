from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_hello_world():
    print("Hello, World!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=90),
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    catchup=False, # Don’t run previous and backfill; run only latest
    schedule_interval=timedelta(seconds=30),
)

hello_world_task = PythonOperator(
    task_id='print_hello_world',
    python_callable=print_hello_world,
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()
