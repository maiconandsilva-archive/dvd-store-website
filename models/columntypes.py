# THIRD PARTY IMPORTS
from flask.globals import g
import six
import sqlalchemy_utils
import passlib.exc

# LOCAL IMPORTS


class CustomPassword(sqlalchemy_utils.Password):
    """Fixes #12 issue from Github"""
    def __eq__(self, value):
        try:
            return super().__eq__(value)
        except passlib.exc.UnknownHashError:
            # If password is unencrypted, check equality
            # between what was supposed to be the hash and the :value
            value = value.encode('utf-8')
            password_match = self.hash == value
            if password_match:
                self.hash = self.context.hash(value)
                if isinstance(self.hash, six.string_types):
                    self.hash = self.hash.encode('utf-8')
                self.changed()
            return password_match


class PasswordType(sqlalchemy_utils.PasswordType):
    def process_result_value(self, value, dialect):
        "Override method from PasswordType to return CustomPasswordType"
        "CustomPassword is only used when loading from the database"
        if value is not None:
            return CustomPassword(value, self.context)
        

class EmailType(sqlalchemy_utils.EmailType):
    def process_result_value(self, value, dialect):
        return value

class EncryptedType(sqlalchemy_utils.EncryptedType):    
    def process_result_value(self, value, dialect):
        if g.allowdecryption:
            return super().process_result_value(value, dialect)
        return None