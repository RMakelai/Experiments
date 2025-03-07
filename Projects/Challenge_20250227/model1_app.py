# Create REST API
from flask import Flask, request, jsonify
import pandas as pd
import pickle
import threading

app = Flask(__name__)

# Load the model
with open('model1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the dataset
data = pd.read_csv('x_test.csv', header=None)

# Manually assign column names
column_names = [f'COL{i}' for i in range(1, 1001)] + ['ID']
data.columns = column_names

@app.route('/predictions/<user_id>', methods=['GET'])
def get_prediction(user_id):
    # Find the user data by ID
    user_data = data[data['ID'] == user_id]
    
    if user_data.empty:
        return jsonify({"error": "User ID not found"}), 404
    
    # Drop the ID column and get the features
    features = user_data.drop(columns=['ID'])
    
    # Make a prediction
    prediction = model.predict(features)
    
    # Return the prediction as JSON
    return jsonify({"class": int(prediction[0])})

def run_app():
    app.run(debug=True, port=5005, use_reloader=False)

if __name__ == '__main__':
    threading.Thread(target=run_app).start()