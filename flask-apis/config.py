import os
from datetime import timedelta
''
class Config:
    DEBUG = True
    """Used for local db file
    basedir = '../' #change
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{student}:{password}@{host}'.format(
        student='',
        password='',
        host='db-postgresql-is-5600-22-do-user-12767037-0.b.db.ondigitalocean.com:25060/neeharchaluvadi'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'neeharchaluvadi'
    JWT_ERROR_MESSAGE_KEY = 'message'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
