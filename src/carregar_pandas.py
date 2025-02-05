import pandas as pd
from sqlalchemy import create_engine

# URL de conexão
DATABASE_URL = "postgresql://ativdade_es2_user:odYsCJpkj3ui0qPNh9Ij9SYT43D9vgg8@dpg-cubpdf9u0jms73bvcko0-a.oregon-postgres.render.com/ativdade_es2"

# Criar engine de conexão
engine = create_engine(DATABASE_URL)

# Executar a consulta e carregar no Pandas
query = "SELECT * FROM issues;"
df = pd.read_sql(query, engine)

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Fechar conexão
engine.dispose()
