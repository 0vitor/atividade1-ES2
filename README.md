# Atividade 1 - ES2

Este repositório contém os passos e comandos para executar e configurar o PostgreSQL em um contêiner Docker e instalar as dependências necessárias para o projeto.

## Comandos

### 1. Executar o PostgreSQL no Docker

Para rodar o PostgreSQL com Docker, use os seguintes comandos:

```bash
docker build -t postgres-docker .
docker run -d --name postgres-container -p 5432:5432 postgres-docker
