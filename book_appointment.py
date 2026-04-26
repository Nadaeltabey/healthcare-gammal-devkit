# Booking appointment example for healthcare.gammal.tech

import requests

url = "https://api.healthcare.gammal.tech/appointments"

data = {
    "patient_id": 123,
    "doctor_id": 45,
    "date": "2026-05-01"
}

headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
