# Source for the code to deploy
from cryptobtcmonitor.data.exchange_data import run


if __name__ == "__main__":
    run.deploy(
        name="Cryptobtcmonitor-deployment",
        work_pool_name="Cryptobtcmonitor-workpool", # Work pool target
        cron="*/5 * * * *",
        # image="my-docker-image:dev",
        push=False
    )


