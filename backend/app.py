
from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle
import mlflow
from sklearn.ensemble import RandomForestClassifier
import joblib  # For loading the scaler

app = Flask(__name__)

# Load the trained model
with open(r'C:\Users\areej\OneDrive\Desktop\mlops-project\models\trained_classifier.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the scaler (pre-trained during model training)
scaler = joblib.load(r'C:\Users\areej\OneDrive\Desktop\mlops-project\models\scaler.pkl')  # Load the scaler saved during training

# Weather condition mapping from your model training
weather_condition_map = {
    0: 'broken clouds', 1: 'clear sky', 2: 'few clouds', 3: 'heavy intensity rain', 4: 'light rain',
    5: 'light snow', 6: 'moderate rain', 7: 'overcast clouds', 8: 'scattered clouds', 9: 'snow'
}

@app.route('/')
def home():
    return render_template('index.html')  # The HTML form page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input from the form
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        wind_speed = float(request.form['wind_speed'])

        # Preprocess the input data (same as during training)
        input_data = pd.DataFrame([[temperature, humidity, wind_speed]], columns=['Temperature', 'Humidity', 'Wind Speed'])
        
        # Transform the input data using the pre-trained scaler
        input_data[["Temperature", "Humidity", "Wind Speed"]] = scaler.transform(input_data[["Temperature", "Humidity", "Wind Speed"]])

        # Make the prediction using the model
        prediction = model.predict(input_data)

        # Map the predicted label to the weather condition
        predicted_weather = weather_condition_map[prediction[0]]

        # Generate the prediction (this is just an example)
        print(f"Prediction:{predicted_weather}\n Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s")

        # prediction_output = f"Prediction: {predicted_weather}, Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s"
        prediction_output = f"Prediction: {predicted_weather}"

        return jsonify({"prediction": prediction_output}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
