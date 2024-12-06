from workflows.mlflow.mlflow_setup import log_parameters_and_metrics

# Example parameters, metrics, and model
params = {"learning_rate": 0.01, "epochs": 10}
metrics = {"accuracy": 0.85, "loss": 0.15}
model_path = "models/trained_model.pkl"

# Log data to MLflow
log_parameters_and_metrics(params, metrics, model_path)
print("Parameters and metrics logged to MLflow!")
