import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "WHATEVER_USERNAME"
TOKEN = "CREATE_TOKEN"
GRAPH = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating a user on pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Mi",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Creating a graph on pixela
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you cycle today? ")
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

# Creating a pixel on Pixela
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

pixel_update_config = {
    "quantity": "15.5"
}

# Updating a pixel on Pixela
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
# response = requests.put(url=pixel_update_endpoint, headers=headers, json=pixel_update_config)

# Deleting a pixel onm Pixela
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=pixel_delete_endpoint, headers=headers)

print(response.text)



