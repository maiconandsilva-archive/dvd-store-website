# THIRD PARTY IMPORTS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

# LOCAL IMPORTS
import models.base

# Flask Settings

app = Flask(__name__)

cfg = import_string(os.environ.get('FLASK_APPSETTINGS'))()
app.config.from_object(cfg)

# SQLAlchemy settings 

db = SQLAlchemy(app, model_class=models.base.BaseModel)

# Azure settings
if os.environ.get('SECRET_VAULT_URI'):
    __default_credential = DefaultAzureCredential()
    
    secret_vault_client = SecretClient(
        os.environ['SECRET_VAULT_URI'],
        __default_credential, logging_enable=True)
    
elif app.config.get('FLASK_ENV') != 'production':
    # Writes key in file for development. No need to create an Azure account
    import helpers
    secret_vault_client = helpers.SecretClient(
        os.environ['SECRET_VAULT_FILE_DEV'])
    
else:
    raise RuntimeError('Using Key file for storage in production is not allowed')
