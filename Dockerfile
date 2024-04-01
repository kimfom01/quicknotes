FROM python:3.12.2-alpine

WORKDIR /app

COPY ./src/requirements.txt .

RUN pip install -r ./requirements.txt

COPY ./src .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]