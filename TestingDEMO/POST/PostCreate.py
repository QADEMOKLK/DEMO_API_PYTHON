import requests
import json

url = "https://reqres.in/api/users"

payload = json.dumps({
  "name": "morpheus",
  "job": "leader"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
