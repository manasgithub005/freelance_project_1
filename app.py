from flask import Flask, jsonify, request
import pickle
import glob
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
# Define model features for each model
model_features = {
    'chiller_power': ['Chiller Loading Chiller'],
    'COND_WF': ['Output Frequency CP 1','Output Frequency CP 2']
    # Add more models and their features as needed
}

# Find all files ending with _env_model.p in a specific directory
model_files = glob.glob('chiller_power/*_env_model.p')

# Load pickle files into models dictionary
models = {}
for file_path in model_files:
    # Extract the key from the file name (assuming the key is before '_env_model.p')
    key = file_path.split('/')[-1].split('_env_model.p')[0]
    with open(file_path, 'rb') as f:
        models[key] = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    predictions = {}
    for model_name, model in models.items():
        model_features_list = model_features.get(model_name, [])
        if not model_features_list:
            predictions[model_name] = 'No features provided'
            continue

        # Extract features for the specific model
        features = [data[model_name].get(feature, 0.0) for feature in model_features_list]

        # Make predictions using the loaded model
        prediction = model.predict([features])
        predictions[model_name] = float(prediction[0])  # Individual prediction as a float

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
