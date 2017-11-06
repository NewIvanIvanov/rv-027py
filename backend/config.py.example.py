# Rename this file to config.py and fill SQLALCHEMY_DATABASE_URI with your's data.


class Config(object):
    DEBUG = False

    SECRET_KEY = 'SECRET_OR_NOT_KEY'

    WTF_CSRF_ENABLED = True

    WTF_CSRF_SECRET_KEY = 'SECRET_OR_NOT_KEY'

    # Change database credentials to yours.
    SQLALCHEMY_DATABASE_URI = 'postgres://user:password@localhost/db_name'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


# password hashing rounds
BCRYPT_LOG_ROUNDS = 14
