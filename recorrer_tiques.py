import os
from dotenv import load_dotenv
from jira import JIRA, Issue

# Configurar la conexión a JIRA

url = os.getenv("JIRA_URL")
api_key = os.getenv("JIRA_API_KEY")

# Conectar a JIRA

jira = JIRA(url, token_auth=api_key)

# Obtener todos los tickets
project_key = "TLP20OPE"
jql = "project = '{}'".format(project_key)
issues = jira.search_issues(jql)

# Imprimir información de los tickets
for issue in issues:
    # Obtener el historial de cambios
    changelog = issue.fields.status

    # Imprimir información básica del ticket
    print("ID:", issue.key)
    print("Tipo", issue.fields.issuetype)
