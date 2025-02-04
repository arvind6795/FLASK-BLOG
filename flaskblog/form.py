from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, file_allowed
from wtforms import (BooleanField, PasswordField, StringField, SubmitField,
                     TextAreaField)
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
    
class UpdateAccountForm(FlaskForm):
    username=StringField('username',validators=[data_required(),length(min=2,max=20)])
    email=StringField('email',validators=[data_required(),Email()])
    picture=FileField('Update picture',validators=[file_allowed(['jpg', 'png'])])
    submit=SubmitField('Update')
    
    def validate_username(self, username):
        if username.data!=current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken.Please choose a different one.')
    def validate_email(self, email):
        if email.data!=current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken.Please choose a different one.')
            
class PostForm(FlaskForm):
    title=StringField('Title',validators=[data_required()])
    content=TextAreaField('Content',validators=[data_required()])
    submit=SubmitField('Post')

class RequestResetForm(FlaskForm):
    email=StringField('email',validators=[data_required(),Email()])
    submit=SubmitField('Request Password Reset')
    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with this email!.')

class ResetPasswordForm(FlaskForm):
    password=PasswordField('password',validators=[data_required(),])
    confirm_password=PasswordField('Confirm password',validators=[data_required(),EqualTo('password')])
    submit=SubmitField('Reset Password')