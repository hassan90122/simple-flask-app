FROM python:3.9-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the app files into the container
COPY . .

# Expose the Flask app's port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

