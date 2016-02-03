from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Required, Email, NumberRange

class LoginForm(Form):
    email = StringField('Enter Your Email Address',validators=[Required(),Email()])
    passw = PasswordField('Enter Your Password',validators=[Required()])
    submit = SubmitField('Login')
    
class RegisterForm(Form):
    email = StringField('Give Your Email Address',validators=[Required(),Email()])
    passw = PasswordField('Give Password',validators=[Required()])
    submit = SubmitField('Register')
    
class FriendsForm(Form):
    name = StringField('Give  Friend name',validators=[Required()])
    address = StringField('Give  Friend Address',validators=[Required()])
    age =  IntegerField('Give Friend Age',validators=[Required(),NumberRange(min=0,max=115,message="Enter age between 0-115")])
    #user_id =  IntegerField('User Id')
    submit = SubmitField('Save')