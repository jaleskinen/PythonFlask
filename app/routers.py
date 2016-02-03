"""Search from app directory app module (now found from __init__.py)"""
from app import app
#render_template gives you access to Jinja2 template
from flask import render_template, request, make_response, flash, redirect, session
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
        #print('login render_template template_index.html')
        return render_template('template_index.html', form=login, islogged=False)
    else:
        #Check if form data is valid
        if login.validate_on_submit():
            #print('login: ' + login.email.data)
            #Check if correct username and password
            user = Users.query.filter_by(email=login.email.data).filter_by(passw=login.passw.data)
            #print('user')
            #print(user[0])
            #print(user)
            if user.count() == 1:
                #login_user(user.one())
                session['user_id'] = user[0].id
                session['user_email'] = user[0].email
                session['islogged'] = True
                #Hae ystävät, tapa 1
                allfriends = Friends.query.filter_by(user_id=user[0].id)
                #print(allFriends)
                return render_template('template_friends.html', islogged=True, allfriends=allfriends)
                #return redirect('/friends')
            else:
                flash('Wrong username or password')
                return redirect('/')
        else:
            #Form data is not valid
            flash('Give proper information to email and password fields')
            return render_template('template_index.html', form=login, islogged=False)

@app.route('/register',methods=['GET','POST'])
def registerUser():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('template_register.html', form=form, islogged=False)
    else:
        if form.validate_on_submit():
            user = Users(form.email.data, form.passw.data)
            try:
                db.session.add(user)
                db.session.commit()
            except:
                #rollback call is not mandatory, flask will do this anyway
                db.session.rollback()
                flash('Username allready in use')
                return render_template('template_register.html', form=form, islogged=False)
            flash('Name {0} registered'.format(form.email.data))
            return redirect('/')
        else:
            flash('Invalid email address or no password given')
            return render_template('template_register.html', form=form, islogged=False)
    
@app.route('/addfriends',methods=['GET','POST'])
def addFriend():
    #Check that user has logged in before you let execute
    if not['islogged' in session] or session['islogged'] == False:
        return redirect('/')
    form = FriendsForm()
    if request.method == 'GET':
        #print(userid)
        return render_template('template_addFriends.html', form=form, islogged=True)
    else:
        if form.validate_on_submit():
            temp = Friends(form.name.data, form.address.data, form.age.data,session['user_id'])
            db.session.add(temp)
            db.session.commit()
            #tapa2
            user = Users.query.get(session['user_id'])
            #print(user.friends)
            #flash('Name {0} added'.format(form.name.data))
            return render_template('template_friends.html', islogged=True, allfriends=user.friends)
        else:
            flash('Wrong name, address or age given')
            return render_template('template_addFriends.html', form=form, islogged=True)
        
@app.route('/logout')
def logout():
    #Delete user session (clear all values)
    session.clear()
    return redirect('/')
            
@app.route('/user/<name>')
def user(name):
    print("User-Agent: " + request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

#Example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)
