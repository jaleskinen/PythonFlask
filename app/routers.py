"""Search from app directory app module (now found from __init__.py)"""
from app import app

#This is comment also, but you can use # only in one line comments

@app.route('/')
def index():
    return 'Hellou World!'

#print('This is not any more included in index() function')
