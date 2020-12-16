FROM python:3.8 AS base

ENV PORT 5000


FROM base AS python-deps

WORKDIR /app

# Install pip requirements
RUN python -m venv /.venv
RUN bash /.venv/bin/activate

COPY requirements.txt ./
RUN pip install -r requirements.txt


FROM python-deps AS backend

WORKDIR /app

COPY --from=python-deps /.venv  /.venv
COPY . .

RUN bash /.venv/bin/activate

ENTRYPOINT [ "./entrypoint.sh" ]
