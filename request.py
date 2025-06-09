import requests

# Sample input of exactly 40 features
sample_features = [
    80, 17, 119893441, 309629, 0, 9908128, 32, 32.0, 0.0, 0.0, 0.0, 82641.11796,
    2582.534936, 387.2176967, 11125.35538, 591274, 0, 120000000, 387.2176967,
    11125.35538, 591274, 0, 0.0, 0.0, 0, 2477032, 0, 2582.534936, 0.0, 32, 32,
    32.00010335, 32.0, 0.0, 309629, 9908128, -1, -1, 309628, 8
]

url = "http://ddos-detector.onrender.com/predict" 

payload = {
    "features": sample_features
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("✅ Prediction:", response.json())
else:
    print("❌ Error:", response.status_code, response.text)
