import requests, json

url = "https://catfact.ninja/fact?max_length=500"

response = requests.request("GET", url=url)
data = json.loads(response.text)
print(data["fact"])