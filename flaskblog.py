from flask import Flask,render_template,url_for

app = Flask(__name__) ## (__name__) to determine the root path of the application
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

if __name__ == "__main__":
    app.run(debug=True)