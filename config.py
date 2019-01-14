class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI= 'mysql+mysqlconnector://root:1998maletaMVM++@localhost/python'
    SECRET_KEY = 'secret_key'
    SECURITY_PASSWORD_SALT='salt'
    SECURITY_PASSWORD_HASH='sha512_crypt'