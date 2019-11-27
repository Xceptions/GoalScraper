from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import sys
sys.path.insert(0, "./src/")
from goal_crawler import CrawlLiveScores

default_args = {
    "start_date": datetime(2019, 10, 6),
    "email": ["agbokenechukwu.k@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 0,
    "retry_delay": timedelta(minutes=3)
}

dag = DAG(
    "project_pipeline",
    description="running the goal crawler",
    schedule_interval="@weekly",
    default_args=default_args,
    catchup=False
)

with dag:
    run_goal_crawler = PythonOperator(task_id="run_goal_crawler",
                                      python_callable=CrawlLiveScores)