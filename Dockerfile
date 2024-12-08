# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the backend code, frontend templates, static files, and models into the container
COPY backend/ ./backend/
COPY frontend/templates/ ./frontend/templates/
COPY frontend/static/ ./frontend/static/
COPY models/ ./models/
# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Set the default command to run the Flask app
CMD ["python", "backend/app.py"]