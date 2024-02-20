import requests

# Configurar la conexión a Jira
url = ""
token = ""

# Generar la solicitud HTTP
headers = {
    "Authorization": "Bearer {}".format(token),
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Decodificar la respuesta JSON
    issue = response.json()

    # Imprimir información del ticket
    print("ID:", issue['id'])
    print("Resumen:", issue['fields']['summary'])
    print("Descripción:", issue['fields']['description'])
else:
    print("Error al obtener la información del ticket:", response.status_code)