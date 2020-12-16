# THIRD PARTY IMPORTS
from flask import Blueprint


app = Blueprint('app', __name__)
app.config = {}

@app.record
def get_config(settup):
    app.config.update(settup.app.config)