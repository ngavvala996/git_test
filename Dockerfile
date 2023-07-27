# Use the official Python Docker image as the base
FROM python:latest
# Set the working directory inside the container
WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt .
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the entire project directory into the container
COPY . .
# Run the pytest command
CMD ["pytest"]
