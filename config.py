import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://username:password@localhost/liquor_store')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
