import os

TESTING = bool(os.environ.get('TESTING', False))
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')
SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
SQLALCHEMY_TRACK_MODIFICATIONS = False
YANDEX_TOKEN = os.environ["YANDEX_TOKEN"]
UPLOAD_DIR = os.environ["UPLOAD_DIR"]
