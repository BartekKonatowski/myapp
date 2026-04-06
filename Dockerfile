FROM python:3.15.0a7-trixie

WORKDIR /app
COPY app/ .

RUN pip install psycopg2-binary
CMD ["python", "app.py"]