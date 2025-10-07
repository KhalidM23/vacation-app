
from flask import Flask, render_template, request, redirect, url_for
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vacations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vacation')
def vacation():
    return render_template('vacations.html')

@app.route('/create_vacation')
def create_vacation():
    return render_template('create_vacation.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    username = request.form['username']
    password = request.form['password']
    return redirect(url_for('vacation'))



with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)