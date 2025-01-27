from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) ## (__name__) to determine the root path of the application
app.config['SECRET_KEY'] ='053cef18c8b4a5275844424b6a7339de'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
from flaskblog import routes
