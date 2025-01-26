
# Use a imagem oficial do PostgreSQL como base
FROM postgres:15

# Configure variáveis de ambiente para o banco de dados
ENV POSTGRES_USER=my_user
ENV POSTGRES_PASSWORD=my_password
ENV POSTGRES_DB=my_database

# Copie os scripts de inicialização (opcional)
# Se você tiver scripts SQL para configurar tabelas ou dados iniciais, copie-os para o diretório padrão de inicialização do PostgreSQL
# ADD ./init-scripts/*.sql /docker-entrypoint-initdb.d/

# Exponha a porta padrão do PostgreSQL
EXPOSE 5432
