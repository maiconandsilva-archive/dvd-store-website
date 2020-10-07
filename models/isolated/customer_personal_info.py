from app import db

class CustomerPersonalInfo(db.Model):
    __bind_key__ = 'db_isolated'
    