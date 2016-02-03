from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Required, Email

class LoginForm(Form):
    email = StringField('Enter Your Email Address',validators=[Required(),Email()])
    passw = PasswordField('Enter Your Password',validators=[Required()])
    submit = SubmitField('Login')
    
class RegisterForm(Form):
    email = StringField('Give Your Email Address',validators=[Required(),Email()])
    passw = PasswordField('Give Password',validators=[Required()])
    submit = SubmitField('Register')
    
class FriendsForm(Form):
    name = StringField('Give Your Friend ame',validators=[Required()])
    address = StringField('Give Your Friend Address')
    age =  IntegerField('Give Your Friend Age')
    user_id =  IntegerField('User Id')
    submit = SubmitField('Save')