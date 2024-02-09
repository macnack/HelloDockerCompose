# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# PYTHONUNBUFFERED=1 is used to avoid buffering the output of the python script
ENV PYTHONUNBUFFERED=1 

# Command to run the script
CMD ["python", "./main.py"]
