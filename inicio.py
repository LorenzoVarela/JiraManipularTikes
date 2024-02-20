from jira import JIRA, Issue
from jira.exceptions import JIRAError
import csv


USER = ""
PASS = ""
URL = ""
PROYECTO = "PIC"

#URL de JIRA
url = URL



#usuario y contraseña
username = USER
password = PASS

#Creamos una instancia de Jira    
try:
    jira = JIRA(url, auth=(username, password))
except JIRAError as e:
    print("Acceso denegado a JIRA:", e)
    exit()


# Filtrar tickets por proyecto
project_key = PROYECTO

jql = "project = '{}'".format(project_key)
tickets = jira.search_issues(jql)

# Imprimir información de los tickets
for ticket in tickets:
    print("ID:", ticket.id)
    print("Fecha y hora de creación:", ticket.fields.created)
    # Obtener la fecha y hora de la transición del estado ESP. ASISTENCIA al estado 1º NIVEL

    #histories = jira.issue(ticket.key)

    print("-----------------")
# Exportar a CSV (opcional)


