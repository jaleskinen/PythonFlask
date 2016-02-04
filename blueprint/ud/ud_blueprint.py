from flask import Blueprint, session, redirect,request,render_template,flash,url_for
from app.forms import FriendsForm
from app.db_models import db
from app.db_models import Users
from app.db_models import Friends

#Create Blueprint
#First argument is the name of the blueprint folder
#Second is always __name__ attribute
#Third parameter tells what folder contains our templates
ud = Blueprint('ud',__name__,template_folder='templates',url_prefix=('/app/'))

#/app/delete router
@ud.route('delete/<int:id>')
def delete(id):
    return "Delete"

@ud.route('update')
def update():
    return "Update"

@ud.route('addfriends',methods=['GET','POST'])
def addFriend():
    #Check that user has logged in before you let execute
    #if not('islogged' in session) or (session['islogged'] == False):
    #    return redirect('/')
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
            print(user.friends)
            #flash('Name {0} added'.format(form.name.data))
            return render_template('template_friends.html', islogged=True, allfriends=user.friends)
        else:
            flash('Wrong name, address or age given')
            return render_template('template_addFriends.html', form=form, islogged=True)

def before_request():
    if not 'islogged' in session:
        return redirect('/')
    
ud.before_request(before_request)