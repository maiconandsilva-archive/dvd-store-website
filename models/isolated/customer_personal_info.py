# THIRD PARTY IMPORTS
from flask.globals import session
from sqlalchemy_utils.types.encrypted.encrypted_type import FernetEngine
from cryptography.fernet import Fernet
import sqlalchemy_utils as su

# LOCAL IMPORTS
from extensions import db
from .. import columntypes as ct


def _get_customer_personal_info(ColumnType, engine, key):
    """
    Generate CustomerPersonalInfo Model with the same key generation function
    for every column
    """
    class CustomerPersonalInfo(db.Model):
        """
        Customer's personal info encrypted on an isolated database
        """
        __bind_key__ = 'db_isolated'
        __tablename__ = 'customers_personal_info'

        customerid = db.Column('customerid', db.Integer, primary_key=True)
        firstname = db.Column(ColumnType(db.String(50), key, engine))
        lastname = db.Column(ColumnType(db.String(50), key, engine))
        address1 = db.Column(ColumnType(db.String(50), key, engine))
        address2 = db.Column(ColumnType(db.String(50), key, engine))
        city = db.Column(ColumnType(db.String(50), key, engine))
        zip = db.Column(ColumnType(db.String(25), key, engine))
        creditcardtype = db.Column(ColumnType(db.Integer, key, engine))
        creditcard = db.Column(ColumnType(db.String(50), key, engine))
        creditcardexpiration = db.Column(ColumnType(db.String(50), key, engine))
        phone = db.Column(ColumnType(
            su.PhoneNumberType(max_length=50), key, engine), unique=True)
        
        email = db.Column(su.EmailType(50), unique=True)
        password = db.Column(su.PasswordType(schemes=['pbkdf2_sha512']))
        more = db.relationship('Customers', primaryjoin=\
            'CustomerPersonalInfo.customerid == Customers.customerid',
            foreign_keys=[customerid])
        
    return CustomerPersonalInfo


def _get_key():
    """Get current key from session or generate it randomly"""
    return session.setdefault('cryptkey', Fernet.generate_key())

CustomerPersonalInfo = \
    _get_customer_personal_info(ct.EncryptedType, FernetEngine, _get_key)