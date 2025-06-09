from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

# Label mapping
label_mapping = {
    0: "Benign",
    1: "DDoS attack HOIC",
    2: "DDoS attack LOIC UDP"
}

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DDoS Prediction API</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }
            .card {
                background-color: rgba(255, 255, 255, 0.05);
                padding: 3em;
                border-radius: 20px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.3);
                max-width: 600px;
                transition: transform 0.3s ease;
            }
            .card:hover {
                transform: scale(1.02);
            }
            h1 {
                font-size: 2.8em;
                margin-bottom: 0.3em;
            }
            p {
                font-size: 1.2em;
                line-height: 1.5;
            }
            code {
                background-color: rgba(0,0,0,0.3);
                padding: 0.2em 0.5em;
                border-radius: 5px;
                font-size: 1.05em;
            }
            .footer {
                margin-top: 2em;
                font-size: 0.9em;
                color: #ccc;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 DDoS Prediction API</h1>
            <p>
                Welcome to the DDoS Detection API.<br><br>
                To use this API, send a <strong>POST</strong> request to <code>/predict</code><br>
                with a JSON body containing exactly <strong>40</strong> numerical features:<br><br>
                <code>{ "features": [val1, val2, ..., val40] }</code><br><br>
                Output will be:<br>
                <code>0 = Benign</code>, <code>1 = DDoS HOIC</code>, <code>2 = DDoS LOIC UDP</code>
            </p>
            <div class="footer">
                Made with ❤️ using Flask & ML
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({'error': 'Missing "features" key in request'}), 400

        features = data['features']
        if not isinstance(features, list) or len(features) != 40:
            return jsonify({'error': 'Input must be a list of exactly 40 numerical features'}), 400

        features_np = np.array(features).reshape(1, -1)
        features_scaled = scaler.transform(features_np)
        prediction = model.predict(features_scaled)[0]

        return jsonify({
            'predicted_class_id': int(prediction),
            'predicted_label': label_mapping.get(prediction, "Unknown")
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
