from flask_sqlalchemy import SQLAlchemy

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
    # Your job: Define the columns here
    # Use: db.Column() with types like db.Integer, db.String(), db.Text, db.Date
    # Example: id = db.Column(db.Integer, primary_key=True)

class Itinerary(db.Model):
    __tablename__ = "itineraries"
    id = db.Column(db.Integer, primary_key = True)
    activity = db.Column(db.String(100))
    date_of_activity = db.Column(db.Date)
    cost_of_activity = db.Column(db.Float)
    vacation_id = db.Column(db.Integer)

class Users(db.Model):
    __tablename__ = "usernames"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))


