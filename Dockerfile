# Use the official Python Docker image as the base
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project directory into the container
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the pytest command
CMD ["pytest"]
