import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = Flask(__name__) ## (__name__) to determine the root path of the application
app.config['SECRET_KEY'] ='053cef18c8b4a5275844424b6a7339de'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.getenv('MAIL_USER')
app.config['MAIL_PASSWORD']=os.getenv('MAIL_PASS')
mail=Mail(app)
from flaskblog import routes
