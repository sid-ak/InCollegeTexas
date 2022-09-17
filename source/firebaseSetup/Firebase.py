import pyrebase
from .Configuration import config

configuration = config

firebase = pyrebase.initialize_app(configuration)
database = firebase.database()

