import pickle
import pandas as pd

# Load the trained model
with open('models/trained_classifier.pkl', 'rb') as file:
    model = pickle.load(file)

# Weather Condition mapping (from your trained model label encoder)
weather_condition_map = {
   0: 'broken clouds', 1: 'clear sky', 2: 'few clouds', 3: 'heavy intensity rain', 4: 'light rain', 
   5: 'light snow', 6: 'moderate rain', 7: 'overcast clouds', 8: 'scattered clouds', 9: 'snow' 
}

# Test input (replace these values with actual values to test)
test_input_data = {
    'Temperature': [0.22250229147571032],  # Example temperature
    'Humidity': [0.8958333333333334],      # Example humidity
    'Wind Speed': [0.32163742690058483]     # Example wind speed
}

# Convert the test input to a DataFrame (this will ensure the feature names match)
test_input = pd.DataFrame(test_input_data)

# Predict the weather condition
prediction = model.predict(test_input)

# Convert prediction to actual weather condition
predicted_weather = weather_condition_map[prediction[0]]

# Print the actual and predicted values
print(f"Actual Weather Condition: broken clouds")  # Replace with the actual value you're testing
print(f"Predicted Weather Condition: {predicted_weather}")
