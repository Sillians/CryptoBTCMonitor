from prefect import flow

# Source for the code to deploy 
from taskflow import main

if __name__ == "__main__":
    main.deploy(
        name="exchange-data-deployment",
        work_pool_name="exchange-data-work-pool", # Work pool target
        cron="*/5 * * * *"
        # cron="0 1 * * *", # Cron schedule (1am every day)
    )


