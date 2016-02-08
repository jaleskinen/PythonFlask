"""Search from app directory app module (now found from __init__.py)"""
from app import app
#render_template gives you access to Jinja2 template
from flask import render_template, request, make_response, flash, redirect, session
from app.forms import LoginForm, RegisterForm, FriendsForm
from app.db_models import Users
from app.db_models import Friends
from app import db
from flask.ext.bcrypt import check_password_hash

#from sqlalchemy.orm.exc import NoResultFound
#from sqlalchemy.orm.exc import MultipleResultsFound
#from app import login_manager
#from flask.ext.login import login_user,login_required,logout_user,current_user


#This is comment also, but you can use # only in one line comments

#Router must always return something

            
@app.route('/user/<name>')
def user(name):
    print("User-Agent: " + request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

#Example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)
