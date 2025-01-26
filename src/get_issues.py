import requests
from dotenv import load_dotenv
import os

# Para criar o token acesse https://github.com/settings/tokens
# Clique em "Generate new token" e selecione "generate new token (classic)".
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/repos/pandas-dev/pandas/issues"
LABEL = "Bug"
STATE = "closed"
PER_PAGE = 100
TOTAL_ISSUES = 300

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}",
}


def fetch_issues():
    issues = []
    page = 1

    while len(issues) < TOTAL_ISSUES:
        response = requests.get(
            GITHUB_API_URL,
            headers=HEADERS,
            params={
                "state": STATE,
                "labels": LABEL,
                "per_page": PER_PAGE,
                "page": page,
            },
        )

        if response.status_code != 200:
            print(f"Erro: {response.status_code}, {response.text}")
            break

        data = response.json()
        if not data:
            break

        issues.extend(data)
        page += 1

    return issues[:TOTAL_ISSUES]


if __name__ == "__main__":
    issues = fetch_issues()
    print(f"Total de issues baixadas: {len(issues)}")

    import json

    with open("issues_bugs.json", "w", encoding="utf-8") as f:
        json.dump(issues, f, ensure_ascii=False, indent=4)

    print("Issues salvas em 'issues_bugs.json'.")
