FROM python:3.8 AS backend

WORKDIR "$HOME/app"

COPY . .

# Install pip requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "./server.py" ]