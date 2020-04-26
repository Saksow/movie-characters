import os


class Config:
    HOST = os.getenv('APP_HOST', 'localhost')
    PORT = int(os.getenv('APP_PORT', '8000'))


class Development(Config):
    ENV = 'development'
    TESTING = False
    DEBUG = True
