FROM python:3.9

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the backend directory and templates
COPY . .

# Run the Flask app
CMD ["python", "app.py"]
