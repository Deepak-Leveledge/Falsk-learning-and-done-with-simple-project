from flask import Flask,render_template,request
from markupsafe import escape

## WSGI Application
app= Flask(__name__)


@app.route("/")
def welcome():
    return '<HTML><h1>Welcome to Flask</h1></HTML>'


@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "POST":
        name=request.form["name"]
        age=request.form["age"]
        email=request.form["email"]
        return f"Hello {name} your email is {email} and your age is {age}"
        
    return render_template("form.html")


@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method == "POST":
        name=request.form["name"]
        age=request.form["age"]
        email=request.form["email"]
        return f"Hello {name} your email is {email} and your age is {age}"
        
    return render_template("form.html")

    
@app.route("/user")
def user_details():
    return render_template("user.html")













if __name__=="__main__":
    app.run(debug=True)

    #debug == true will reload the server automatically in the browser while just saving the files 