# THIRD PARTY IMPORTS
import os
import base64

# LOCAL IMPORTS


class Settings:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    REPORT_PATH = os.path.join('.app', 'report', 'customer_data')
    APP_TEMPLATE_EXT = '.jinja' # Custom

    SECRET_KEY = os.urandom(32)

    def _database_uri(self, uri, password):
        return uri.format(**os.environ)

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return self._database_uri(
            os.environ['BASE_DB_URI'], os.environ['DB_PASSWORD'])

    @property
    def SQLALCHEMY_BINDS(self):
        return  {
            'db_isolated': self._database_uri(
                os.environ['BASE_ISOLATED_DB_URI'],
                os.environ['ISOLATED_DB_PASSWORD']),
        }


class Dev(Settings):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
    SEND_FILE_MAX_AGE_DEFAULT = 0


class Homolog(Settings):
    FLASK_ENV = 'homolog'
    DEBUG = False
    Testing = True
    

class Prod(Settings):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    
    @property
    def SECRET_KEY(self):
        return base64.b64decode(os.environ['FLASK_SECRET_KEY'])