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
        
        IMPORTANT: md is stands for metadata
        """
        return type(self)
    
    def save(self):
        app.db.session.add(self)
        app.db.session.commit()
        
    def delete(self):
        app.db.session.delete(self)
        app.db.session.commit()
        
    @classmethod
    def from_form(cls, form):
        """Retorna um novo objeto a partir de um form"""
        instance = cls()
        form.populate_obj(instance)
        return instance
        