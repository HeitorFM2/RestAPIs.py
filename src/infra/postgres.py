import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()


class PostgresDatabase:
    def get_connection(self):
        return psycopg2.connect(
            host=os.environ["DB_HOST"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
        )

    def get(self, query: str, params=None) -> list:
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()

    def execute(self, query: str, params=None) -> None:
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            conn.commit()
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()
