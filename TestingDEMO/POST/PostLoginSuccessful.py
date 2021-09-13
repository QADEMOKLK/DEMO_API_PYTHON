import requests
import json

url = "https://reqres.in/api/login"

payload = json.dumps({
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
