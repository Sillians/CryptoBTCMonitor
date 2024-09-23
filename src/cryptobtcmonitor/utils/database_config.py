import os
from utils.database import DBConnection
from core.logger import *

log = Logger("Getting PostgreSQL Data Warehouse Credentials", logging.INFO).get_logger()

def get_postgres_credentials() -> DBConnection:
    log.info('Get Postgres Credentials...')
    return DBConnection(
        db=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER', ''),
        password=os.getenv('POSTGRES_PASSWORD', ''),
        host=os.getenv('POSTGRES_SERVER', ''),
        port=int(os.getenv('POSTGRES_PORT', 5432)),
    )