"""Search from app directory app module (now found from __init__.py)"""
from app import app
#render_template gives you access to Jinja2 template
from flask import render_template, request, make_response, flash, redirect
from app.forms import LoginForm, RegisterForm
from app.db_models import Users
from app import db

#This is comment also, but you can use # only in one line comments

#Router must always return something
@app.route('/',methods=['GET','POST'])
def index():
    login = LoginForm()
    #Check if GET method
    if request.method == 'GET':
        print('login render_template template_index.html')
        return render_template('template_index.html', form=login)
    else:
        #Check if form data is valid
        if login.validate_on_submit():
            print('login: ' + login.email.data)
            print(login.passw.data)
            return render_template('template_user.html')
        else:
            #Form data is not valid
            print('Login Form data is not valid')
            flash('Give proper information to email and password fields')
            return render_template('template_index.html', form=login)

@app.route('/register',methods=['GET','POST'])
def registerUser():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('template_register.html', form=form)
    else:
        if form.validate_on_submit():
            user = Users(form.email.data, form.passw.data)
            db.session.add(user)
            db.session.commit()
            flash('Name {0} registered'.format(form.email.data))
            return redirect('/')
        else:
            flash('Invalid email address or no password given')
            return render_template('template_register.html', form=form)
    
    
            
@app.route('/user/<name>')
def user(name):
    print("User-Agent: " + request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

#Example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)
