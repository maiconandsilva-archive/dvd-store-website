FROM postgres as dellstore

ADD https://git.io/JTdKr /docker-entrypoint-initdb.d/dellstore.sql
RUN chmod 744 /docker-entrypoint-initdb.d/dellstore.sql

FROM postgres as dellstore_isolated

ADD https://git.io/JTdKZ /docker-entrypoint-initdb.d/dellstore_isolated.sql
RUN chmod 744 /docker-entrypoint-initdb.d/dellstore_isolated.sql

FROM python:3.8 AS backend
ARG PYTHON_DEBUG

# Assign value 1 to variables in Debug Mode

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE ${PYTHON_DEBUG}

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED ${PYTHON_DEBUG}

WORKDIR /app

# Switch to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser -m && chown -R appuser /app
USER appuser

# For Azure dependency scripts
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Install pip requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "./server.py" ]