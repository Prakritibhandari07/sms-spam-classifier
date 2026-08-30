# Use a lightweight, official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (this lets Docker cache the pip install step,
# so rebuilds are much faster if you only change your code, not dependencies)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the app: your API code, model, and vectorizer
COPY . .

# Document that this container listens on port 8000
EXPOSE 8000

# Command to run when the container starts
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
