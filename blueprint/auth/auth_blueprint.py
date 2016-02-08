from flask import Blueprint, session, redirect,request,render_template,flash,url_for
from app.forms import LoginForm, RegisterForm
from app.db_models import Users, Friends
from app import db
from flask.ext.bcrypt import check_password_hash

#Create Blueprint
#First argument is the name of the blueprint folder
#Second is always __name__ attribute
#Third parameter tells what folder contains our templates
auth = Blueprint('auth',__name__,template_folder='templates')

@auth.route('/index/<int:page>',methods=['GET','POST'])
@auth.route('/',methods=['GET','POST'])
def index(page=1):
    login = LoginForm()
    if request.method == 'GET' and 'user_id' in session:
        friends = Friends.query.filter_by(user_id=session['user_id']).paginate(page,10,False)
        return render_template('template_friends.html',isLogged=True,friends=friends)
    #Check if GET method
    if request.method == 'GET':
        #print('login render_template template_index.html')
        return render_template('template_index.html', form=login, islogged=False)
    else:
        #Check if form data is valid
        if login.validate_on_submit():
            #Check if correct username
            user = Users.query.filter_by(email=login.email.data)
            #print('user')
            if (user.count() == 1) and (check_password_hash(user[0].passw,login.passw.data)):
                #login_user(user.one())
                session['user_id'] = user[0].id
                #session['user_email'] = user[0].email
                session['islogged'] = True
                #Hae ystävät, tapa 1
                friends = Friends.query.filter_by(user_id=user[0].id).paginate(page,10,False)
                #print(allFriends)
                return render_template('template_friends.html', islogged=True, friends=friends)
                #return redirect('/friends')
            else:
                flash('Wrong username or password')
                return redirect('/')
        else:
            #Form data is not valid
            flash('Give proper information to email and password fields')
            return render_template('template_index.html', form=login, islogged=False)

@auth.route('/register',methods=['GET','POST'])
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
    
        
@auth.route('/logout')
def logout():
    #Delete user session (clear all values)
    session.clear()
    return redirect('/')