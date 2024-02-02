# Domine Apache Airflow. https://www.eia.ai/
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag =  DAG('triggerdag1', description="Trigger DAG",
        schedule_interval=None,start_date=datetime(2023,3,5),
        catchup=False)

task1 = BashOperator(task_id="tsk1",bash_command="sleep 5",dag=dag )
task2 = BashOperator(task_id="tsk2",bash_command="sleep 5",dag=dag )
task3 = BashOperator(task_id="tsk3",bash_command="sleep 5",dag=dag,
                     trigger_rule='one_failed' ) # na prática espera que a tarefa 3 não execute. 

[task1, task2] >> task3