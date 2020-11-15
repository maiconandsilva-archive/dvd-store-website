# THIRD PARTY IMPORTS
from flask.globals import request
from datetime import datetime
from sqlalchemy.orm import backref
import sqlalchemy_utils as su

# LOCAL IMPORTS
from helpers import mask
from app import db
import models.columntypes as customtype
import models.orders # used by 


class Customers(db.Model):
    __tablename__ = 'customers'

    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    customerid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), info={'anonymize': True})
    lastname = db.Column(db.String(50), info={'anonymize': True})
    address1 = db.Column(db.String(50), info={'anonymize': True})
    address2 = db.Column(db.String(50), info={'anonymize': True})
    city = db.Column(db.String(50), info={'anonymize': True})
    state = db.Column(db.String(50), info={'anonymize': True})
    zip = db.Column(db.Integer, info={'anonymize': True})
    country = db.Column(su.CountryType)
    region = db.Column(db.Integer)
    email = db.Column(su.EmailType(50), unique=True)
    phone = db.Column(su.PhoneNumberType(max_length=50), unique=True)
    creditcardtype = db.Column(db.Integer, info={'anonymize': True})
    creditcard = db.Column(db.String(50), info={'anonymize': True})
    creditcardexpiration = db.Column(db.String(50), info={'anonymize': True})
    username = db.Column(db.String(50), info={'anonymize': True})
    password = db.Column(customtype.PasswordType(schemes=['pbkdf2_sha512']))
    age = db.Column(db.Integer, info={'anonymize': True})
    income = db.Column(db.Integer, info={'anonymize': True})
    gender = db.Column(su.ChoiceType(GENDERS, impl=db.String(1)))
    deleted_at = db.Column('deleted_at', db.DateTime)
    shopping_history = db.relationship('Orders', backref='customer')

    @property
    def is_active(self):
        return self.deleted_at is None
  
    @classmethod
    def from_form(cls, form):
        """Retorna um novo Customer a partir de um form"""
        customer = cls()
        form.populate_obj(customer)
        return customer

    def anonymized(self):
        """Anonimiza informacoes que identificam uma pessoa"""
        self._deleted_at = datetime.now()
        self.phone = self.phone and mask(self.phone.e164[1:], 5, 0)
        self.email = self.email and \
            mask(self.email, pattern=mask.EMAIL_ANONYMIZATION, n_mask_char=2)
        self.password = None

        for column in self.__table__.columns:
            if column.info.get('anonymize'):
                setattr(self, column.name, None)
        return self
