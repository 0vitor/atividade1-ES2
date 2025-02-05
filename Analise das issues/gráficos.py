# gráficos.py
import pandas as pd
import matplotlib.pyplot as plt
import ast  # Para converter strings em listas

# Carregar os dados
df = pd.read_csv("issues.csv")

# Remover duplicatas (caso existam)
df = df.drop_duplicates()

# Converter tema_relacionado de string para lista real
def tratar_tema(tema):
    try:
        temas = ast.literal_eval(tema)  # Converte string para lista
        if isinstance(temas, list):
            return temas
        return [tema]  # Se não for lista, transforma em lista
    except:
        return [tema]  # Se houver erro, mantém como lista

df['tema_relacionado'] = df['tema_relacionado'].apply(tratar_tema)

# Converter datas
df['created_at'] = pd.to_datetime(df['created_at'])
df['closed_at'] = pd.to_datetime(df['closed_at'])

# **Usar resolution_time_days corretamente**
df['resolution_time_days'] = pd.to_numeric(df['resolution_time_days'], errors='coerce')

# Explodir temas para separá-los corretamente
df_explodido = df.explode('tema_relacionado')

# 1️⃣ Contagem de Issues por Tema
theme_counts = df_explodido['tema_relacionado'].value_counts()
theme_counts.plot(kind='bar', figsize=(12,6), color='skyblue')
plt.title("Contagem de Issues por Tema")
plt.xlabel("Tema")
plt.ylabel("Número de Issues")
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.subplots_adjust(bottom=0.3)
plt.show()
plt.close()

# 2️⃣ Tempo Médio de Resolução por Tema
average_resolution_time = df_explodido.groupby('tema_relacionado')['resolution_time_days'].mean()
average_resolution_time.plot(kind='bar', figsize=(12,6), color='salmon')
plt.title("Tempo Médio de Resolução por Tema")
plt.xlabel("Tema")
plt.ylabel("Tempo Médio de Resolução (dias)")
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.subplots_adjust(bottom=0.3)
plt.show()
plt.close()

# 3️⃣ Issues por Assignee
# Tratar valores nulos em 'assignee_username'
df['assignee_username'] = df['assignee_username'].fillna("Sem Assignee")

# Contar o número de issues por assignee
assignee_counts = df['assignee_username'].value_counts()

# Criar lista de cores: vermelho para 1 issue, azul para 2 issues, amarelo para o restante
colors = ['red' if count == 1 else 'blue' if count == 2 else 'yellow' for count in assignee_counts]

# Criar o gráfico
fig, ax = plt.subplots(figsize=(12,6))
bars = assignee_counts.plot(kind='barh', color=colors, ax=ax, edgecolor='black')

# Ajustar a largura das barras pequenas para dar mais destaque
for bar, count in zip(bars.patches, assignee_counts):
    if count in [1, 2]:
        bar.set_linewidth(2)  # Adiciona uma borda mais grossa
        bar.set_alpha(0.8)  # Deixa um pouco mais opaco para destaque

# Adicionar rótulos de número apenas nas barras destacadas
for bar, count in zip(bars.patches, assignee_counts):
    if count in [1, 2]:
        ax.text(bar.get_width() + 0.3,  # Posição X do texto
                bar.get_y() + bar.get_height()/2,  # Posição Y do texto
                f"{count}",  # Texto exibido
                va='center', ha='left', fontsize=10, fontweight='bold', color='black')

# Personalização do gráfico
plt.title("Issues por Assignee", fontsize=14)
plt.xlabel("Número de Issues", fontsize=12)
plt.ylabel("Assignee", fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)  # Linhas guias no eixo X
plt.show()
plt.close()

# 4️⃣ Issues Fechadas por Milestone
df['milestone'] = df['milestone'].fillna("Sem Milestone")  # 🔹 Correção do FutureWarning
milestone_counts = df['milestone'].value_counts()
milestone_counts.plot(kind='pie', figsize=(8,8), autopct='%1.1f%%', startangle=90)
plt.title("Distribuição de Issues Fechadas por Milestone")
plt.ylabel("")
plt.show()
plt.close()

# 5️⃣ Issues Abertas por Mês
df['mes_abertura'] = df['created_at'].dt.to_period('M')
monthly_issues = df['mes_abertura'].value_counts().sort_index()
monthly_issues.plot(kind='line', figsize=(10,6), marker='o', color='orange')
plt.title("Número de Issues Abertas por Mês")
plt.xlabel("Mês")
plt.ylabel("Número de Issues")
plt.xticks(rotation=45)
plt.show()
plt.close()
