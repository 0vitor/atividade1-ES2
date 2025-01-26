import psycopg2


def create_tables():
    db_config = {
        "dbname": "my_database",
        "user": "my_user",
        "password": "my_password",
        "host": "localhost",
        "port": "5432",
    }

    sql = "SELECT to_regclass('public.issues');"

    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Executar Query
        cursor.execute(sql)
        conn.commit()
        result = cursor.fetchone()
        print(result)

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    create_tables()
