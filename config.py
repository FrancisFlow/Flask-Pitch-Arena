import os

from instance.config import SECRET_KEY
class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:Master@Work@localhost/pitcharena'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = os.environ.get('SECRET_KEY')


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:Master@Work.2@localhost/pitcharena'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:Master@Work.2@localhost/pitcharena'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:Master@Work.2@localhost/pitcharena'


    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig

}