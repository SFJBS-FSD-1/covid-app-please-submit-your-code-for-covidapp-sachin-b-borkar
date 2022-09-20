import json,requests
from flask import Flask, render_template, request ,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:welcome$1234@localhost/appdb"
db = SQLAlchemy(app)

migrate = Migrate(app,db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    # email = db.Column(db.String(200), unique=True, nullable=False)

#   adding user to table
    @staticmethod
    def add_user(username,password):
        new_user = User(username=username, password=password)
        result = db.session.add(new_user)
        db.session.commit()
        return result

    @staticmethod
    def get_user(username):
         data = User.query.filter_by(username=username).first()
         return data


# homepage
@app.route("/",methods= ["GET","POST"])
def homepage():
        return render_template("homepage.html")

# # login page
# @app.route("/login",methods = ["GET","POST"])
# def login():
#         if request.method == "POST" and 'username' in request.form and 'password' in request.form:
#             username = request.form["username"]
#             User.get_user(username=username)
#             return render_template("login.html")
#         else:
#             return render_template("login.html")

@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username,password)
        check_user = User.get_user(username=username)
        if check_user:
            return render_template("register.html" , status = check_user)
        else:
            status = User.add_user(username=username,password=password)
            return render_template("register.html", status=status)

if __name__ == "__main__":
    app.run(debug=True)