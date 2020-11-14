# THIRD PARTY IMPORTS
from flask_sqlalchemy.model import Model

# LOCAL IMPORTS
import app


class BaseModel(Model):
    @property
    def md(self):
        """
        Return class to gather metadata from the table and column attributes.
        Very useful for using in templates. Better than using instance.__class__
        """
        return type(self)
    
    def save(self):
        app.db.session.add(self)
        app.db.session.commit()
        