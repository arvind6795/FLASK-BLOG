from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import Email, EqualTo, data_required, length


class RegistrationForm(FlaskForm):
    username=StringField('username',validators=[data_required(),length(min=2,max=20)])
    email=StringField('email',validators=[data_required(),Email()])
    password=PasswordField('password',validators=[data_required(),])
    confirm_password=PasswordField('Confirm password',validators=[data_required(),EqualTo('password')])
    submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email=StringField('email',validators=[data_required(),Email()])
    password=PasswordField('password',validators=[data_required(),])
    remeber=BooleanField('Remember me')
    submit=SubmitField('Login')