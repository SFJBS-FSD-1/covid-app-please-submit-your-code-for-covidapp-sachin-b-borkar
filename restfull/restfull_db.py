from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:welcome$1234@localhost/moviesdb"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

# id = db.Column(db.Integer, primary_key=True)  # this is the primary key
# title = db.Column(db.String(80), nullable=False)
# year = db.Column(db.Integer, nullable=False)
# genre = db.Column(db.String(80), nullable=False)


# commands to run sql from python
# from restfull.restfull_db import db
# db.create_all()
# from restfull.restfull_db import Profile
# admin = Profile(username="sachin",email="sachin.borakrb@tcs.com")
# db.session.add(admin)
# db.session.commit()
# Profile.query.all()
# Profile.query.filter_by(username = "rohit").first()
