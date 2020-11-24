# THIRD PARTY IMPORTS
import os

# LOCAL IMPORTS


class Settings:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ['FLASK_SECRET_KEY']
    FLASK_PORT = os.environ['FLASK_PORT']
    REPORT_PATH = os.path.join('.app', 'report', 'customer_data')

    APP_TEMPLATE_EXT = '.jinja' # Custom

    def _database_uri(self, uri, password_file):
        with open(password_file) as password:
            return uri.format(PASSWORD=password.read(), **os.environ)

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return self._database_uri(
            os.environ['BASE_DB_URI'], os.environ['DB_PASSWORD_FILE'])

    @property
    def SQLALCHEMY_BINDS(self):
        return  {
            'db_isolated': self._database_uri(
                os.environ['BASE_ISOLATED_DB_URI'],
                os.environ['ISOLATED_DB_PASSWORD_FILE']),
        }


class Dev(Settings):
    DEBUG = True
    TESTING = True

    SQLALCHEMY_ECHO = True
    
    SEND_FILE_MAX_AGE_DEFAULT = 0