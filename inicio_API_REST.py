import requests
from requests.auth import HTTPBasicAuth


USER = ""
PASS = ""
URL = ""
PROYECTO = ""
Key = ""

# Configurar la conexión a Jira
url = URL
username = USER
password = PASS

# Generar la solicitud HTTP
auth = HTTPBasicAuth(username, password)

headers = {
    "Accept": "application/json"
}

response = requests.get(url, auth=auth, headers=headers)



# Verificar el estado de la respuesta
if response.status_code == 200:
    # Decodificar la respuesta JSON
    print(response.status_code)
    changelog = response.json()

    # Recorrer el historial de cambios
    for history in changelog['histories']:
        # Imprimir la fecha y hora de la transición
        print(history['created'])

        # Imprimir el nombre del usuario que realizó la transición
        print(history['author']['displayName'])

        # Imprimir el campo que cambió y su valor anterior y nuevo
        for item in history['items']:
            print("Campo:", item['field'])
            print("Valor anterior:", item['fromString'])
            print("Valor nuevo:", item['toString'])
            print("-----------------")
else:
    print("Error al obtener el historial de cambios:", response.status_code)
