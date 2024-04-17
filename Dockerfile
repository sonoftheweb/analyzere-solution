# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY compute.py /app/

# Make your program executable
RUN chmod +x /app/compute.py

# Define the entry point from which the script can accept arguments
ENTRYPOINT ["python", "/app/compute.py"]
