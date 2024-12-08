import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import pickle
import mlflow
import mlflow.sklearn

# Load preprocessed data
data = pd.read_csv(r"C:\Users\PC\Downloads\mlops-project\mlops-project\data\processed_data.csv")  # Adjust path as necessary

# Prepare features (X) and target (y)
X = data[['Temperature', 'Humidity', 'Wind Speed']]  # Using all features
y = data['Weather Condition']  # Target is 'Weather Condition'

# Encode target labels (Weather Condition)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)  # Convert categories to numeric labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train a Random Forest Classifier (you can experiment with other models too)
model = RandomForestClassifier(n_estimators=300, random_state=71)
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions, target_names=label_encoder.classes_)

# Save the trained model
model_path = r'C:\Users\PC\Downloads\mlops-project\mlops-project\models\trained_classifier.pkl'
with open(model_path, 'wb') as file:
    pickle.dump(model, file)

# Log training details to MLflow
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("MLOps Project")
with mlflow.start_run(run_name="Model Training and Evaluation"):
    # Log parameters
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_param("test_size", 0.2)
    # Log metrics
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("n_estimators", 100)
    # Log model
    mlflow.sklearn.log_model(model, "model")
    # Save the model artifact path
    mlflow.log_artifact(model_path)

print(f"Model trained and saved to {model_path}")
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)
