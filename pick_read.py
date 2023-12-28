import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from chiller_config import config
import pickle
import os
import sys

import os
import pickle

# Directory containing the models
models_directory = './chiller_power'  # Replace this with your actual directory path
model_files = os.listdir(models_directory)

# Filter model files with suffix '_env_model.p'
env_model_files = [file for file in model_files if file.endswith('_env_model.p')]

# List to store loaded models
loaded_models = []

# Load models
for file_name in env_model_files:
    file_path = os.path.join(models_directory, file_name)
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
        loaded_models.append(model)

print(loaded_models)
# Now loaded_models contains all the loaded models ending with '_env_model.p' in the specified directory


# Function to get predictions from loaded models
def get_predictions(input_data):
    predictions = []
    for model in loaded_models:
        # Make predictions using each loaded model
        # Modify this part based on your model's prediction method
        prediction = model.predict(input_data)  # Assuming input_data is compatible with each model
        predictions.append(prediction)
    return predictions

# Example usage:
input_data = [[81.4],]  # Example input data, modify as per your model's input requirements

# Get predictions using loaded models
predictions = get_predictions(input_data)

# Now 'predictions' contains the results from each loaded model for the given input data
print("Predictions for input data:", predictions)
