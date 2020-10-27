# from wtforms_alchemy import model_form_factory
from flask_wtf import FlaskForm
from app import db

# BaseModelForm = model_form_factory(FlaskForm)

# class ModelForm(BaseModelForm):
#     @classmethod
#     def get_session(self):
#         return db.session

from wtforms_alchemy import ModelForm