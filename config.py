import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///loans.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False