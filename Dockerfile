# Use an official slim Python image as the base image
FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the Python project files into the container
COPY python/ ./python/

# (Optional) If you have a requirements.txt, copy and install dependencies:
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run your Python application.
# Adjust the entry point file and path as needed.
CMD ["python", "./python/main.py"]
