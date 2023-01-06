import requests
from datetime import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "djishokh"
TOKEN = "Djiwan02092002"
GRAPH_ID = "graph1"

# creating our new account
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# parameters for creating our own graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Python Coding",
    "unit": "Hours",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# adding the pixels to our graph
pixel_adding_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.now()

pixel_params = {
    "date": today.strftime("%Y") + today.strftime("%m") + today.strftime("%d"),
    "quantity": input("How many hours did you spend on Python today? ")
}
response = requests.post(url=pixel_adding_endpoint, json=pixel_params, headers=headers)
print(response.text)

# changing the values in the graph using put
pixel_changing_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220106"

pixel_changing_params = {
    "quantity": "0.0"
}

# response = requests.put(url=pixel_changing_endpoint, json=pixel_changing_params, headers=headers)

# deleting the values from the graph using delete
# pixel_deleting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220106"
# response = requests.delete(url=pixel_deleting_endpoint, headers=headers)
