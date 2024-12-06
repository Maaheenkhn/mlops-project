# MLOps Pipeline with MLFlow, Airflow, CI/CD, and Kubernetes Deployment

This project extends the foundational MLOps pipeline by integrating advanced tools and workflows such as MLFlow for model versioning, Airflow for workflow automation, and Docker with Kubernetes for CI/CD and deployment. The goal is to manage datasets, log models, automate workflows, and deploy a full-stack application using modern DevOps/MLOps practices.

## Project Overview

In this project, we will:

- Integrate **MLFlow** for:
  - Versioning models during training.
  - Logging key metrics and parameters.
  - Registering models in the MLFlow Model Registry.
  
- Build a **Full-Stack Application**:
  - **Frontend**: A user interface to input weather features and predict temperatures.
  - **Backend**: A REST API for predictions using Flask or FastAPI.
  - **Database**: User authentication with login, signup, and session management.
  
- Implement a **Branch-Based Workflow**:
  - Use Git branches for development, testing, and production.
  - Set up CI/CD pipelines to automate testing, Docker image creation, and Kubernetes deployment.
  
- Document the implementation in a **Medium blog**.

## Tools & Technologies Used

- **MLFlow**: For model versioning and tracking.
- **DVC**: For managing datasets and models.
- **Airflow**: For automating workflows.
- **Docker**: For containerizing the application.
- **Kubernetes**: For deploying the application in a scalable manner.
- **Flask/FastAPI**: For building the backend API.
- **React/HTML/JS**: For the frontend interface.
- **SQLite/MySQL/MongoDB**: For user authentication and session management.

