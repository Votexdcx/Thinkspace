FROM python:3.12-slim

WORKDIR /backenddjango

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install djangorestframework
COPY . .
ENV DJANGO_ENV=development
EXPOSE ${PORT}
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]




