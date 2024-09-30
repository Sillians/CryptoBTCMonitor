from prefect import flow

# Source for the code to deploy 
import taskflow

if __name__ == "__main__":
    flow.from_source(
        source=taskflow,
        entrypoint="taskflow.py:run", # Specific flow to run
    ).deploy(
        name="exchange-data-deployment",
        work_pool_name="exchange-data-work-pool", # Work pool target
        cron="*/5 * * * *"
        # cron="0 1 * * *", # Cron schedule (1am every day)
    )