import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import mlflow
import joblib

def preprocess_data():
    # Load raw data from CSV
    df = pd.read_csv("data/weather_data.csv")
    
    # Save processed data path
    processed_data_path = "data/processed_data.csv"
    
    try:
        # Try to connect to MLflow
        mlflow.set_tracking_uri("http://localhost:5000")  # MLFlow server URI
        mlflow.set_experiment("MLOps Project")  # Set the experiment name
        
        with mlflow.start_run(run_name="Data Preprocessing"):
            # Handle missing values
            df.fillna(method='ffill', inplace=True)
            
            # Normalize numerical fields
            scaler = MinMaxScaler()
            df[["Temperature", "Humidity", "Wind Speed"]] = scaler.fit_transform(df[["Temperature", "Humidity", "Wind Speed"]])

            # Log parameters
            mlflow.log_param("missing_value_strategy", "ffill")
            mlflow.log_param("scaling_method", "MinMaxScaler")

            # Save processed data
            df.to_csv(processed_data_path, index=False)
            
            # Log processed data artifact
            mlflow.log_artifact(processed_data_path)

            # Save the scaler after fitting on the training data
            joblib.dump(scaler, 'models/scaler.pkl')

            print("Preprocessed data saved and logged to MLflow.")
    
    except Exception as e:
        # In case MLflow isn't running or there is an error, print the error and save the data
        print(f"MLflow error: {e}")
        print("Saving preprocessed data without logging to MLflow.")
        
        # Save the processed data regardless of MLflow error
        df.to_csv(processed_data_path, index=False)
        print(f"Preprocessed data saved to {processed_data_path} without logging to MLflow.")

if __name__ == "__main__":
    preprocess_data()
