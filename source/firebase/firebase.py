import pyrebase
import configuration

firebase = pyrebase.initialize_app(configuration.config)
database = firebase.database()