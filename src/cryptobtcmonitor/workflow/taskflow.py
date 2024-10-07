import datetime
from datetime import timezone, timedelta
import sys
import os
import requests
from cryptobtcmonitor.core.logger import *
from typing import Any, Dict, List, Optional
from prefect import flow, task

import psycopg2.extras as p
from cryptobtcmonitor.utils.database import PostgresConnection
from cryptobtcmonitor.utils.database_config import get_postgres_credentials
from cryptobtcmonitor.data.get_exchange_insert_query import _get_exchange_insert_query

from dotenv import load_dotenv
load_dotenv()
exchange_url=os.getenv('EXCHANGE_URL', '')

log = Logger("Get exchange data and batch upload data to postgres...", logging.INFO).get_logger()


@task(name="Get UTC time", log_prints=True)
def get_utc_from_unix_time(unix_ts: Optional[Any], second: int = 1000) -> Optional[datetime.datetime]:
    return (
        datetime.datetime.fromtimestamp(int(unix_ts) / second, tz=timezone.utc)
        if unix_ts
        else None
    )
    
    
@task(name="Get the exchange data information", log_prints=True, cache_expiration=timedelta(30))
def get_exchange_data() -> List[Dict[str, Any]]:
    log.info("Getting the exchange data from coincap...")
    try:
        r = requests.get(exchange_url)
    except requests.ConnectionError as ce:
        log.error((f"There was an error with the request, {ce}"))
        sys.exit(1)
    return r.json().get('data', [])


@flow(log_prints=True, retries=3, description="My flow to Get Exchange Data and create connection to the Postgres Database")
def main() -> Dict:
    data = get_exchange_data()
    for d in data:
        d['update_dt'] = get_utc_from_unix_time(d.get('updated'))
        log.info("Get all exchange data...")
    with PostgresConnection(get_postgres_credentials()).managed_cursor() as curr:
        p.execute_batch(curr, _get_exchange_insert_query(), data)


if __name__ == '__main__':
    main.serve(name="exchange-data-deployment",
              tags=['ExchangeDataDeploymentSession'],
              cron="*/5 * * * *")