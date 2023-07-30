# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . .

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
