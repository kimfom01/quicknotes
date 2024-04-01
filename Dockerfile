# FROM python:3.12.2-alpine
# FROM python:slim-bullseye
FROM python

WORKDIR /app

EXPOSE 5000

COPY ./src/requirements.txt .

RUN pip install -r ./requirements.txt

COPY ./src .


# CMD [ "gunicorn ", "app:app" ]
# CMD [ "python", "./app.py" ]

ENTRYPOINT [ "python" ]

CMD ["app.py" ]