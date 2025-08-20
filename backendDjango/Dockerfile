FROM python:3.12.11-slim-trixie

WORKDIR /backendDjango


RUN pip3 install django==5.1
COPY . .
ENV DJANGO_ENV=development
EXPOSE ${PORT}
CMD ["python3", "manage.py", "runserver", "0.0.0.0:4567"]




