import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_postgres():
    while True:
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="123456",
                host="db",  # Nombre del servicio del contenedor en docker-compose.yml
                port="5432",
                database="prueba"
            )
            connection.close()
            print("PostgreSQL is ready!")
            break
        except OperationalError:
            print("PostgreSQL is not ready yet, retrying in 1 second...")
            time.sleep(1)

if __name__ == "__main__":
    wait_for_postgres()
