

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    USR = 'root'
    PWD = 'mohan1111'
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@localhost:3306/exercise'.format(USR, PWD)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
