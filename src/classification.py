import json
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
import os

from urllib.parse import urlparse

# URL de conexão
db_url = os.getenv("DB_URL")

# Separar os componentes da URL
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


def insert_issue(cursor, issue_data):
    insert_query = """
        INSERT INTO issues (
            title,
            body,
            created_at,
            closed_at,
            resolution_time_days,
            milestone,
            author_username,
            assignee_username,
            tema_relacionado,
            url_issue
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        );"""
    cursor.execute(
        insert_query,
        (
            issue_data["title"],  # title
            issue_data["body"],  # body
            issue_data["created_at"],  # created_at
            issue_data["closed_at"],  # closed_at
            issue_data["resolution_time_days"],  # resolution_time_days
            issue_data["milestone"],  # milestone
            issue_data["author_username"],  # author_username
            issue_data["assignee_username"],  # assignee_username
            issue_data["tema_relacionado"],  # tema_relacionado
            issue_data["url"],  # url_issue
        ),
    )


def get_temas():
    print("Classifique os temas relacionados à issue:")
    print("(i) Arquitetura de software")
    print("(ii) Padrões e Estilos Arquiteturais")
    print("(iii) Padrões de Projeto")
    temas = input(
        "Digite os números dos temas separados por vírgula (exemplo: 1,2,3): "
    )
    temas_selecionados = []

    if "1" in temas:
        temas_selecionados.append("Arquitetura de software")
    if "2" in temas:
        temas_selecionados.append("Padrões e Estilos Arquiteturais")
    if "3" in temas:
        temas_selecionados.append("Padrões de Projeto")

    return temas_selecionados


def processar_issues():
    conn = connect_db()
    cursor = conn.cursor()

    json_file_path = "../data/issues_bugs.json"
    with open(json_file_path, "r") as f:
        issues = json.load(f)
    print(len(issues))
    for issue in issues:
        print(f"Processando issue: {issue['title']}")
        print(issue.get("html_url"))
        tema_relacionado = get_temas()

        created_at = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        closed_at = datetime.strptime(issue["closed_at"], "%Y-%m-%dT%H:%M:%SZ")
        resolution_time = closed_at - created_at
        resolution_time_days = resolution_time.days
        created_at_str = created_at.strftime("%Y-%m-%d %H:%M:%S")
        closed_at_str = closed_at.strftime("%Y-%m-%d %H:%M:%S")

        milestone = issue.get("milestone")
        if milestone is None:
            print(f"Warning: 'milestone' is None for issue {issue.get('id')}")
        milestone_title = (
            milestone.get("title") if isinstance(milestone, dict) else None
        )
        issue_data = {
            "title": issue["title"],
            "body": issue["body"],
            "created_at": created_at_str,
            "closed_at": closed_at_str,
            "resolution_time_days": resolution_time_days,
            "milestone": milestone_title,
            "author_username": issue["user"]["login"],
            "assignee_username": (
                issue.get("assignee")["login"] if issue.get("assignee") else None
            ),
            "tema_relacionado": tema_relacionado,
            "url": issue["html_url"],
        }

        insert_issue(cursor, issue_data)
        conn.commit()

        print(f"Issue '{issue['title']}' inserida com sucesso!\n")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    processar_issues()
