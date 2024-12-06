import mlflow
import mlflow.sklearn

# Set MLflow Tracking URI
mlflow.set_tracking_uri("http://localhost:5000")

# Start an MLflow experiment
mlflow.set_experiment("MLOps Project")

def log_parameters_and_metrics(params, metrics, model_path):
    with mlflow.start_run():
        # Log parameters
        for key, value in params.items():
            mlflow.log_param(key, value)
        
        # Log metrics
        for key, value in metrics.items():
            mlflow.log_metric(key, value)
        
        # Log model
        mlflow.sklearn.log_model(model_path, "model")
