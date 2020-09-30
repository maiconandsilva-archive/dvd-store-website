
import os

class Settings:
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False