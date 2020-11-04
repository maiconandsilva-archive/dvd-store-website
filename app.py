from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from werkzeug.utils import import_string

import os

# Flask Settings

app = Flask(__name__)

cfg = import_string(os.environ.get('FLASK_APPSETTINGS'))()
app.config.from_object(cfg)

# SQLAlchemy settings 

class BaseModel(Model):
    def save(self):
        db.session.add(self)
        db.session.commit()

db = SQLAlchemy(app, model_class=BaseModel)