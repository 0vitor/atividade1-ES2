import psycopg2
from dotenv import load_dotenv
import os
from urllib.parse import urlparse

load_dotenv()

db_url = os.getenv("DB_URL")

if db_url is None:
    raise ValueError("A variável de ambiente DB_URL não foi encontrada.")

result = urlparse(db_url)

if not all([result.username, result.password, result.hostname, result.path]):
    raise ValueError("A URL de conexão do banco de dados está incompleta.")

dbname = result.path[1:]
user = result.username
password = result.password
host = result.hostname
port = result.port or 5432


def connect_db():
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
            sslmode="require",
        )
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise


try:
    connection = connect_db()
    print("Conexão com o banco de dados estabelecida com sucesso!")

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM issues")
        resultado = cursor.fetchall()
        print(resultado)

    connection.close()

except Exception as e:
    print(f"Ocorreu um erro ao tentar conectar: {e}")
