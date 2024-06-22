# Use the official lightweight Python image based on Alpine Linux
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Define a volume for data persistence
VOLUME /app/data

# Expose the port
EXPOSE $PORT

# Command to run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
