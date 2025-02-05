from sqlalchemy import create_engine
import pandas as pd

# URL do BD PostgreSQL
db_url = 'postgresql://ativdade_es2_user:odYsCJpkj3ui0qPNh9Ij9SYT43D9vgg8@dpg-cubpdf9u0jms73bvcko0-a.oregon-postgres.render.com/ativdade_es2'

# Criar a conexão usando SQLAlchemy
engine = create_engine(db_url)

try:
    # Executar consulta e carregar no Pandas
    df = pd.read_sql("SELECT * FROM issues", engine)

    # Exibir o número total de issues carregadas
    print(f"Total de issues carregadas: {len(df)}")

    # Salvar os dados como CSV
    df.to_csv("issues.csv", index=False)
    print("✅ Dados salvos como 'issues.csv' com sucesso!")

    # Verificar o número de issues no CSV
    df_csv = pd.read_csv("issues.csv")
    print(f"Total de issues no CSV: {len(df_csv)}")
    print(df.columns)  # Exibe os nomes das colunas


except Exception as e:
    print(f"🚨 Erro ao consultar o banco: {e}")

finally:
    # Fechar a conexão
    engine.dispose()
    print("🔌 Conexão com o banco fechada.")
