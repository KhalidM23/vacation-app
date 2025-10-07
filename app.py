
from flask import Flask, render_template, request, redirect, url_for
from models import db, Vacation
from flask_login import LoginManager, UserMixin, login_user, logout_user, \
                        login_required, current_user
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-me'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vacations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app)
login_manager.login_view = 'login'


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vacations')
def vacations():
    vacations = Vacation.query.all()
    print(f"Number of vacations: {len(vacations)}")  # Debug line
    for v in vacations:
        print(f"Destination: {v.destination}")  # Debug line
    return render_template('vacations.html',vacations=vacations)

@app.route('/create_vacation', methods=['POST','GET'])
def create_vacation():
    if(request.method == 'POST'):
        dest = request.form.get('destination')
        start_date_str = request.form.get('start_date')
        st_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()


        end_date_str = request.form.get('end_date')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()


        cost = request.form.get('total_cost')
        tips = request.form.get('tips')
        user = 1
        new_vacay = Vacation(destination = dest,start_date = st_date, end_date = end_date,
                             total_cost = cost, tips = tips)
        db.session.add(new_vacay)
        db.session.commit()
        print("Vacation saved successfully!")
        print(f"Total vacations in DB: {Vacation.query.count()}")
        return redirect(url_for('vacations'))
    return render_template('create_vacation.html')
    











@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    #query to find the usernames from it
    username = request.form['username']
    password = request.form['password']
    return redirect(url_for('vacation'))

@app.route('/login_user', methods=['POST'])
def login_user():


    return redirect(url_for('vacation'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




if __name__ == '__main__':
    app.run(debug=True)