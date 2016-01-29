from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email

class LoginForm(Form):
    email = StringField('Enter Your Email Address',validators=[Required(),Email()])
    passw = PasswordField('Enter Your Password',validators=[Required()])
    submit = SubmitField('Login')
    
class RegisterForm(Form):
    email = StringField('Give Your Email Address',validators=[Required(),Email()])
    passw = PasswordField('Give Password',validators=[Required()])
    submit = SubmitField('Register')