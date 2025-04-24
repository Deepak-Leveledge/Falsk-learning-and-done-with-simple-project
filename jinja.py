##Building the URL Dynamically
## Jinja 2 Template Engine
## variable rule 
### jinja 2 template engine they have multiple way 
'''
1. {{ }} - used to print the value of a variable
2. {% %} - used to write control statements like if, for, etc.
'''


from flask import Flask,render_template,request,redirect,url_for
from markupsafe import escape

## WSGI Application
app= Flask(__name__)


@app.route("/")
def welcome():
    return '<HTML><h1>Welcome to Flask</h1></HTML>'


@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")





# @app.route("/submit",methods=["GET","POST"])
# def submit():
#     if request.method == "POST":
#         name=request.form["name"]
#         age=request.form["age"]
#         email=request.form["email"]
#         return f"Hello {name} your email is {email} and your age is {age}"
        
#     return render_template("getresult.html")

## variable Rule
@app.route("/success/<int:score>")
def success(score):
    # return f"Your score is {score}"
    result=''
    if score>60 and score<70:
        result="You have passed the exam"
    elif score>70 and score<80:
        result="You have passed the exam with good marks "
    else:
        result="You have failed the exam"
    return render_template("result.html",result=result)



@app.route("/successPATH/<int:score>")
def successPATH(score):
    # return f"Your score is {score}"
    result=''
    if score>60 and score<70:
        result="You have passed the exam"
    elif score>70 and score<80:
        result="You have passed the exam with good marks "
    else:
        result="You have failed the exam"
    exp={"score":score ,
     "result":result}
    return render_template("sucess.html",result=exp)


@app.route("/fail/<int:score>")
def fail(score):

    return render_template('result.html',result=score)


@app.route('/getresult',methods=["GET","POST"])
def get_result():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['data_science'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template("getresult.html")
    return redirect(url_for('successPATH',score=total_score))



@app.route("/user")
def user_details():
    return render_template("user.html")













if __name__=="__main__":
    app.run(debug=True)

    #debug == true will reload the server automatically in the browser while just saving the files 