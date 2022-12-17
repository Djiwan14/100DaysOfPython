import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
latitude = response.json()["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
coordinates = (latitude, longitude)
print(coordinates)
