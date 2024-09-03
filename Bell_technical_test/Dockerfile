# Use an official Python runtime as the base image
FROM python:3.8-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Specify the command to run the application when the container starts
CMD ["python", "rest_server.py"]

