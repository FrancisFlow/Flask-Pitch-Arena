import os

from instance.config import SECRET_KEY
class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:human2@localhost/pitcharena'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:human2@localhost/pitcharena'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:human2@localhost/pitcharena'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:human2@localhost/pitcharena'


    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig

}