import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):

    # Set a secret key as environment variable to protect forms & encode JWT tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # If no database is provided as environment variable, I will use a sqlite db called 'app.db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail configuration - for capabilities such as error logging & reset pass capability
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['tommyvandezande@gmail.com']

    # Interface
    POSTS_PER_PAGE = 25

    # Translations
    LANGUAGES = ['en', 'nl']

    # MS Azure Translation service
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')