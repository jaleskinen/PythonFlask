from flask import Flask
from flask.ext.bootstrap import Bootstrap

#This Flask(__name__) is flask package name, now it is 'app'.
app = Flask(__name__)

#This lines configures our app using the config.py file
app.config.from_object('config')
bootstrap = Bootstrap(app)
from app import routers