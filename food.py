from flask import *
import mysql.connector
from mysql.connector import *

db=connect(host='localhost',user='root',password='welcome123')
a=db.cursor()
a.execute("create database if not exists nivi")
db=connect(host='localhost',user='root',password='welcome123',db="nivi")
a=db.cursor()
a.execute("create table if not exists nivi1(email_id varchar(50),password varchar(30))")

db.commit()


myapp=Flask(__name__)
myapp.secret_key="wel"


@myapp.route("/")
def button():
    return render_template("food.html")

@myapp.route("/fir")
def first():
    return render_template("food.login.html")

@myapp.route("/log",methods=["POST","GET"])
def log():
    if request.method=="POST":
        m=request.form["email"]
        p=request.form["password"]
        a.execute("select * from nivi1 where email_id=%s and password=%s",(m,p))
        s=a.fetchall()
        if s:
            return render_template("food.content.html")
        else:
            return "failed"
    else:
        return render_template(("finalfood.html"))

@myapp.route("/order")
def ord():
    return render_template("finalfood.html")


@myapp.route("/sec")
def second():
    return render_template("food.sign.html")

@myapp.route("/signup",methods=["POST","GET"])
def signup():
    if request.method=="POST":
        m=request.form["email"]
        p=request.form["password"]
        s=a.execute("insert nivi1(email_id,password) values(%s,%s)",(m,p))
        db.commit()
        return render_template("food.login.html")
    else:
        return "wrong method"


myapp.run(debug=True)
