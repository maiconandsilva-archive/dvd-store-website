FROM postgres as dellstore

COPY sql/dellstore.sql /docker-entrypoint-initdb.d/dellstore.sql
COPY sql/dellstore_MOD.sql /usr/src/dellstore_MOD.sql

FROM postgres as dellstore_isolated

COPY sql/dellstore_isolated.sql /usr/src/dellstore_isolated.sql

FROM python:3.7 AS backend

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT [ "python" ]
CMD [ "./run.py" ]