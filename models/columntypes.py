# THIRD PARTY IMPORTS
from flask.globals import g
import sqlalchemy_utils

# LOCAL IMPORTS

class EncryptedType(sqlalchemy_utils.EncryptedType):    
    def process_result_value(self, value, dialect):
        if g.allowdecryption:
            return super().process_result_value(value, dialect)
        return None