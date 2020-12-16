# THIRD PARTY IMPORTS
from flask_sqlalchemy.model import Model

# LOCAL IMPORTS
import extensions as exts


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
        exts.db.session.add(self)
        exts.db.session.commit()
        
    def delete(self):
        exts.db.session.delete(self)
        exts.db.session.commit()
        
    @classmethod
    def from_form(cls, form):
        """Retorna um novo objeto a partir de um form"""
        instance = cls()
        form.populate_obj(instance)
        return instance
        