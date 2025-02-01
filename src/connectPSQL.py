import psycopg2
from urllib.parse import urlparse

db_url = "postgresql://ativdade_es2_user:odYsCJpkj3ui0qPNh9Ij9SYT43D9vgg8@dpg-cubpdf9u0jms73bvcko0-a.oregon-postgres.render.com/ativdade_es2"

result = urlparse(db_url)
dbname = result.path[1:]
user = result.username
password = result.password
host = result.hostname
port = result.port


def connect_db():
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port,
        sslmode="require",
    )
