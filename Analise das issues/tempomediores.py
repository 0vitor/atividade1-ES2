# gráficos.py
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("issues.csv")

# Verificar as primeiras linhas do DataFrame
print(df.head())  # Apenas para debug

# Converte as colunas de data para datetime
df['created_at'] = pd.to_datetime(df['created_at'])
df['closed_at'] = pd.to_datetime(df['closed_at'])

# Calcular o tempo de resolução
df['tempo_resolucao'] = (df['closed_at'] - df['created_at']).dt.days

# Calcular o tempo médio de resolução por tema
average_resolution_time = df.groupby('tema_relacionado')['tempo_resolucao'].mean()

# Criar o gráfico
average_resolution_time.plot(kind='bar', figsize=(10,6), color='salmon')
plt.title("Tempo Médio de Resolução por Tema")
plt.xlabel("Tema")
plt.ylabel("Tempo Médio de Resolução (dias)")
plt.xticks(rotation=45, ha="right")
plt.show()
