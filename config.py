"""
Application Configurations

"""

#Main App Configuration
DEBUG = True
SECRET_KEY = "findyourdoctor"

#SQLAlchemy Configuration
SQLALCHEMY_DATABASE_URI = "sqlite:///findyourdoctor.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False