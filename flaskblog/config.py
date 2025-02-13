import os

from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY ='f386095c82439349a787ceb8487493eb' #os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ="sqlite:///site.db"   #os.getenv('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USER')
    MAIL_PASSWORD = os.getenv('MAIL_PASS')