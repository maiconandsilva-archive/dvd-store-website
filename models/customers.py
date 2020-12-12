# THIRD PARTY IMPORTS
from models.isolated.customer_personal_info import CustomerPersonalInfo
from datetime import datetime
import sqlalchemy_utils as su

# LOCAL IMPORTS
from helpers import mask
from app import db
import models.columntypes as customtype
import models.orders # used by SQLAlchemy


class Customers(db.Model):
    __tablename__ = 'customers'

    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    customerid = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50))
    country = db.Column(su.CountryType)
    age = db.Column(db.Integer)
    income = db.Column(db.Integer)
    gender = db.Column(su.ChoiceType(GENDERS, impl=db.String(1)))
    deleted_at = db.Column('deleted_at', db.DateTime)
    shopping_history = db.relationship('Orders', backref='customer')

    @property
    def is_active(self):
        return self.deleted_at is None

    def inactivated(self):
        """Atualiza status usuário como deletado"""
        self.deleted_at = datetime.now()
        return self