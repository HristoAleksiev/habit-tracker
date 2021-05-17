import requests
import os

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
pixel_table_header = {
    "X-USER-TOKEN": TOKEN,
}

pixela_endpoint = "https://pixe.la/v1/users"
acc_registration_args = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_table_args = {
    "id": "running",
    "name": "Running Distance Tracking",
    "unit": "Km",
    "type": "float",
    "color": "kuro",
}
pixela_push_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{pixel_table_args['id']}"
pixela_push_pixel_args = {
    "date": "20210411",
    "quantity": "12",
}

response = requests.post(url=pixela_push_pixel_endpoint, json=pixela_push_pixel_args, headers=pixel_table_header)
print(response.text)
