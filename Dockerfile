# Use an official slim Python image as the base image
FROM python:3.14.0b3-slim-bullseye

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory inside the container
WORKDIR /app

# Copy the Python project files into the container
COPY python/ ./python/

# (Optional) If you have a requirements.txt, copy and install dependencies:
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint to run the Python application
ENTRYPOINT ["python", "./python/main.py"]

# Set the default arguments for the application
CMD ["--repo-url", "https://github.com/charlesastokes/IaC-Gitlab-Bot.git", "--commit-sha1", "abc123", "--commit-sha2", "def456"]