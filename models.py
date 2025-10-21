from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Vacation(db.Model):

    __tablename__ = "vacations"
    id = db.Column(db.Integer,primary_key =True)
    destination = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    total_cost = db.Column(db.Float)
    tips = db.Column(db.Text)
    user_id = db.Column(db.Integer)

class Itinerary(db.Model):
    __tablename__ = "itineraries"
    id = db.Column(db.Integer, primary_key = True)
    activity = db.Column(db.String(100))
    date_of_activity = db.Column(db.Date)
    cost_of_activity = db.Column(db.Float)
    vacation_id = db.Column(db.Integer)


class Bookmarks(db.Model):
    __tablename__ = "bookmarks"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    vacation_id = db.Column(db.Integer)

class User(db.Model,UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),nullable = False, unique = True)
    password_hash = db.Column(db.String(255),nullable = False)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash, password)


