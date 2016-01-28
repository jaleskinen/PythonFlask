"""Search from app directory app module (now found from __init__.py)"""
from app import app
#render_template gives you access to Jinja2 template
from flask import render_template, request, make_response
from app.forms import LoginForm

#This is comment also, but you can use # only in one line comments

#Router must always return something
@app.route('/',methods=['GET','POST'])
def index():
    login = LoginForm()
    return render_template('template_index.html', form=login)

@app.route('/user/<name>')
def user(name):
    print("User-Agent: " + request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

#Example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)
    
#print('This is not any more included in index() function')
