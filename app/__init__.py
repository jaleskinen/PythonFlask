from flask import Flask
from flask.ext.bootstrap import Bootstrap
#from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

#This Flask(__name__) is flask package name, now it is 'app'.
app = Flask(__name__)

#This lines configures our app using the config.py file
app.config.from_object('config')
bootstrap = Bootstrap(app)
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'root'

db = SQLAlchemy(app)
from app import routers