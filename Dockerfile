# Use the official Python Docker image as the base
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project directory into the container
COPY . .

# Run the pytest command
CMD ["pytest"]
