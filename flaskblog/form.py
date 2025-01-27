from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import (Email, EqualTo, ValidationError, data_required,
                                length)

from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username=StringField('username',validators=[data_required(),length(min=2,max=20)])
    email=StringField('email',validators=[data_required(),Email()])
    password=PasswordField('password',validators=[data_required(),])
    confirm_password=PasswordField('Confirm password',validators=[data_required(),EqualTo('password')])
    submit=SubmitField('Sign Up')
    
    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken.Please choose a different one.')
    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken.Please choose a different one.')

class LoginForm(FlaskForm):
    email=StringField('email',validators=[data_required(),Email()])
    password=PasswordField('password',validators=[data_required(),])
    remember=BooleanField('Remember me')
    submit=SubmitField('Login')