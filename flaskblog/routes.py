from flask import flash, redirect, render_template, url_for

from flaskblog import app, bcrypt, db
from flaskblog.form import LoginForm, RegistrationForm
from flaskblog.models import Post, User

app.app_context().push()

posts=[
    {
        'author':'Elliot Alderson',
        'title':'Blog post 1',
        'content':'First blog content',
        'date_posted':'April 20, 2025'
    },
    {
        'author':'Percy jackson',
        'title':'Blog post 2',
        'content':'Second blog content',
        'date_posted':'April 21, 2025'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template ("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)
@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='Admin@11':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html',title='Login',form=form)