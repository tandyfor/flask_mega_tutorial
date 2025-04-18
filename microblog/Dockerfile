FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev 
RUN pip install psycopg2

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
COPY .env .env
COPY .flaskenv .flaskenv
RUN chmod a+x boot.sh

ENV FLASK_APP microblog.py
RUN flask translate compile

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]