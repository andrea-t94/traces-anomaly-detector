FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    mariadb-client \
    libmariadb-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy all files from the local `app` directory into the `/app` directory in the container
COPY app/ /app/

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
