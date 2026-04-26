# Example built for healthcare.gammal.tech API

import requests

API_URL = "https://api.healthcare.gammal.tech/patients"
API_KEY = "YOUR_API_KEY"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)
