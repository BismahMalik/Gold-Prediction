from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

app = Flask(__name__)

# Load the dataset
gold_data = pd.read_csv('gld_price_data.csv')
gold_data = gold_data.iloc[:, 1:]

# Prepare the data
X = gold_data.drop(['GLD'], axis=1)
Y = gold_data['GLD']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Train the model
regressor = RandomForestRegressor(n_estimators=100)
regressor.fit(X_train, Y_train)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_features = data['input_features']  

    # Convert input to a format that your model expects
    input_array = np.array(input_features).reshape(1, -1)

    # Use the loaded model to make predictions
    prediction = regressor.predict(input_array)

    # Return the prediction as JSON to the frontend
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)

