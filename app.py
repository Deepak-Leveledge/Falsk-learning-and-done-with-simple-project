from flask import Flask
from markupsafe import escape

## WSGI Application
app= Flask(__name__)

## Basic Route
@app.route('/')
def welcome():
    return 'Hello, Welcome to the Flask App World!'

@app.route('/about')
def about():
    return "This is my About page"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)} How are you!"


@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return f"User {escape(username)}"



@app.route("/projects")
def projects():
    return "The project with  single /"


@app.route("/projects/")
def projects():
    return "The project page"





if __name__=="__main__":
    app.run(debug=True)

    #debug == true will reload the server automatically in the browser while just saving the files 