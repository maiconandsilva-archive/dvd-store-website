FROM postgres as dellstore

COPY sql/dellstore.sql /docker-entrypoint-initdb.d/dellstore.sql
COPY sql/dellstore_MOD.sql /usr/src/dellstore_MOD.sql

FROM postgres as dellstore_isolated

COPY sql/dellstore_isolated.sql /usr/src/dellstore_isolated.sql

FROM python:3.7 AS backend

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install pip requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Switch to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

ENTRYPOINT [ "python" ]
CMD [ "./app.py" ]