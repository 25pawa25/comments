import backoff
import psycopg2
from django.db.backends.postgresql.base import DatabaseWrapper as PostgresDatabaseWrapper

from backend.components.database import WAIT_DB_TIMEOUT


class DatabaseWrapper(PostgresDatabaseWrapper):
    @backoff.on_exception(backoff.expo, psycopg2.OperationalError, max_time=WAIT_DB_TIMEOUT, raise_on_giveup=True)
    def get_new_connection(self, conn_params):
        return super().get_new_connection(conn_params)
