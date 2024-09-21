from contextlib import contextmanager
from dataclasses import dataclass
import psycopg2
from psycopg2 import Error
from core.logger import *

log = Logger("Creating PostgreSQL Data Warehouse Connection", logging.INFO).get_logger()

@dataclass
class DBConnection:
    """A class for holding the database connection details"""
    db: str
    user: str
    password: str
    host: str
    port: int = 5432
    

class PostgresConnection:
    """
    DATABASE_URL=postgres://{user}:{password}@{hostname}:{port}/{database-name}
    """
    
    def __init__(self, db_conn: DBConnection) -> None:
        self.conn_url = (
            f'postgresql://{db_conn.user}:{db_conn.password}@'
            f'{db_conn.host}:{db_conn.port}/{db_conn.db}'
        )
        
    @contextmanager
    def managed_cursor(self, cursor_factory=None):
        self.conn = psycopg2.connect(self.conn_url)
        self.conn.autocommit = True
        log.info("Create a cursor to perform database operations")
        self.curr = self.conn.cursor(cursor_factory=cursor_factory)
        log.info("Connection to database established")
        try:
            yield self.curr
        except (Exception, Error) as error:
            log.info("Error while connecting to PostgreSQL", error)
        finally:
            self.curr.close()
            self.conn.close()
