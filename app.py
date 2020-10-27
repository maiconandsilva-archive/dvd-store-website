from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

import os

app = Flask(__name__)

cfg = import_string(os.environ.get('FLASK_APPSETTINGS'))()
app.config.from_object(cfg)

db = SQLAlchemy(app)