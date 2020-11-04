# THIRD PARTY IMPORTS
from flask_sqlalchemy.model import Model

# LOCAL IMPORTS
import app


class BaseModel(Model):
    def save(self):
        app.db.session.add(self)
        app.db.session.commit()
        