
from flask import Flask, render_template
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vacations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vacation')
def vacations():
    return render_template('vacations.html')

with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)