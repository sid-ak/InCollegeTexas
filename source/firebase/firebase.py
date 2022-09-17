import pyrebase
from firebase.Configuration import config

configuration = config

firebase = pyrebase.initialize_app(configuration)
database = firebase.database()

