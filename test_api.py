import requests

data = {"features": [6.5, 0.3, 0.4, 2.0, 0.05, 35.0, 130.0, 0.994, 5, 0.9, 14]}
response = requests.post("http://localhost:8000/predict", json=data)
print(response.json())
