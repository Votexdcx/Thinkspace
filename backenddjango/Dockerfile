FROM python:3.12-slim

# Install dependencies including PostgreSQL client
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /backenddjango

# Copy requirements and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of your code
COPY . .

# Environment
ENV DJANGO_ENV=development

# Expose the port
EXPOSE 8000

# Run Django dev server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


