from flask import Flask,render_template
from markupsafe import escape

## WSGI Application
app= Flask(__name__)


@app.route("/")
def welcome():
    return '<HTML><h1>Welcome to Flask</h1></HTML>'


@app.route("/index")
def index():
    return render_template("index.html")\
    
@app.route("/user")
def user_details():
    return render_template("user.html")













if __name__=="__main__":
    app.run(debug=True)

    #debug == true will reload the server automatically in the browser while just saving the files 