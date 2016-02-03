"""Search from app directory app module (now found from __init__.py)"""
from app import app
#render_template gives you access to Jinja2 template
from flask import render_template, request, make_response, flash, redirect
from app.forms import LoginForm, RegisterForm, FriendsForm
from app.db_models import Users
from app.db_models import Friends
from app import db
#from sqlalchemy.orm.exc import NoResultFound
#from sqlalchemy.orm.exc import MultipleResultsFound
#from app import login_manager
#from flask.ext.login import login_user,login_required,logout_user,current_user


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
            user = Users.query.filter_by(email=login.email.data).filter_by(passw=login.passw.data)
            if user.count() == 1:
                #login_user(user.one())
                return redirect('/friends')
            else:
                flash('Invalid username or password')
                return redirect('/')
        else:
            #Form data is not valid
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

@app.route('/friends',methods=['GET','POST'])
def friends():
    form = FriendsForm()
    if request.method == 'GET':
        #print(username)
        return render_template('template_friends.html', form=form)
    else:
        if request.form['submit'] == 'Add Friend':
            print('add friend ')
            return redirect('/addfriends')
        elif request.form['submit'] == 'Log Out':
            print('logout ')
            return redirect('/')
        
    
    
@app.route('/addfriends',methods=['GET','POST'])
def addFriend():
    form = FriendsForm()
    if request.method == 'GET':
        print(userid)
        return render_template('template_addFriends.html', form=form, user=username)
    else:
        if form.submit():
            friend = Friends(form.name.data, form.address.data, form.age.data, user_id=userid)
            db.session.add(friend)
            db.session.commit()
            flash('Name {0} added'.format(form.name.data))
            return render_template('template_friends.html', form=form)
        else:
            flash('Invalid nane, address or age given')
            return render_template('template_addFriends.html', form=form)
    
    
            
@app.route('/user/<name>')
def user(name):
    print("User-Agent: " + request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

#Example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)
