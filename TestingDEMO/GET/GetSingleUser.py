import requests

url = "https://reqres.in/api/users/2"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
