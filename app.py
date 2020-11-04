# THIRD PARTY IMPORTS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string
import os

# LOCAL IMPORTS
import models.base

# Flask Settings

app = Flask(__name__)

cfg = import_string(os.environ.get('FLASK_APPSETTINGS'))()
app.config.from_object(cfg)

# SQLAlchemy settings 

db = SQLAlchemy(app, model_class=models.base.BaseModel)