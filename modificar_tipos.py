import os
from dotenv import load_dotenv
from jira import JIRA
from jira.exceptions import JIRAError


tickets_dict = {
    'TLP20OPE-387':'Despliegue SVA'
    ,'TLP20OPE-372':'Usuarios SVA'
}

url = os.getenv("JIRA_URL")
api_key = os.getenv("JIRA_API_KEY")

try:
    jira = JIRA(url, token_auth=api_key)
except JIRAError as e:
    print("Acceso a Jira denegado:", e)
    exit()

for ticket_key, ticket_type in tickets_dict.items():
    try:
        issue = jira.issue(ticket_key)
        issue.update(fields={"issuetype": {"name": ticket_type}})
        print(f"'{ticket_key}': Tipo de ticket '{ticket_type}' actualizado a '{ticket_type}'.")
    except JIRAError as e:
        print(f"Error al actualizar el ticket '{ticket_key}':", e)