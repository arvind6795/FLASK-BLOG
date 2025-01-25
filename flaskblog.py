from flask import Flask, flash, redirect, render_template, url_for

from form import LoginForm, RegistrationForm

app = Flask(__name__) ## (__name__) to determine the root path of the application

app.config['SECRET_KEY'] ='053cef18c8b4a5275844424b6a7339de'
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
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
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
if __name__ == "__main__":
    app.run(debug=True)