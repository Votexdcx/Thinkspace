FROM python:3.12.11-slim-trixie

WORKDIR /backend-Django


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV DJANGO_ENV=development
EXPOSE ${PORT}
CMD ["python3", "-m", "django", "run", "--host=0.0.0.0", "--port = 4567"]




