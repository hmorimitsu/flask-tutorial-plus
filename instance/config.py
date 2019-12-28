import os

DEBUG = True

CSRF_ENABLED = True

# Replace the keys below by a secret random key!
CSRF_SESSION_KEY = 'secret'
SECRET_KEY = 'secret'
# CSRF_SESSION_KEY = os.environ['SECRET_KEY']
# SECRET_KEY = os.environ['SECRET_KEY']

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = 'postgres://my_user:my_password@localhost:5432/flaskr'
DATABASE_URL = 'sqlite:///{}/flaskr.db'.format(BASE_DIR)

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
