FROM python:3.8.10-slim-buster

WORKDIR /app

COPY ./src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP="src/api.py"
ENV FLASK_DEBUG=1

EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0" ]docker