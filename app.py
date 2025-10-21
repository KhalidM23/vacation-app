
from multiprocessing import synchronize
from xmlrpc.client import _datetime
from flask import Flask, render_template, request, redirect, url_for
from models import Itinerary, db, Vacation
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vacations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

#                                                                   VACATION INFORMATION

@app.route('/vacations')
def vacations():
    vacations = Vacation.query.all()
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

        new_vacay = Vacation(destination = dest,start_date = st_date, end_date = end_date,
                             total_cost = cost, tips = tips)
        db.session.add(new_vacay)
        db.session.commit()

        return redirect(url_for('vacations'))
    return render_template('create_vacation.html')
   
    
@app.route('/edit_vacation/<int:vacation_id>', methods = ['POST','GET'])
def reroute_edit_vacation(vacation_id):
    vacation = Vacation.query.get(vacation_id)
    print(vacation.destination)
    return render_template('edit_vacation.html', vacation = vacation)

@app.route('/edit_vacationXXX/<int:vacation_id>', methods=['GET',"POST"])
def edit_vacation(vacation_id):
    if(request.method == 'POST'):
        editted_vacation = Vacation.query.get(vacation_id)
        editted_vacation.destination = request.form.get('destination')

        start_date_str = request.form.get('start_date')
        editted_vacation.start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()


        end_date_str = request.form.get('end_date')
        editted_vacation.end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        

        editted_vacation.total_cost = request.form.get('total_cost')
        editted_vacation.tips = request.form.get('tips')
 
        db.session.commit()
        return render_template('home.html', vacation=editted_vacation)
    return render_template('home.html', vacation=editted_vacation)


@app.route('/view_vacation/<int:vacation_id>', methods= ['GET'])
def view_vacation(vacation_id):
    vacation = Vacation.query.get(vacation_id)
    itineraries = Itinerary.query.filter_by(vacation_id=vacation_id).all()
    return render_template('view_vacation.html', vacation = vacation, itineraries = itineraries)


@app.route('/delete_vacation/<int:vacation_id>', methods=['POST'])
def delete_vacation(vacation_id):
    vacation = Vacation.query.get(vacation_id)
    db.session.query(Itinerary).filter_by(vacation_id=vacation_id).delete(synchronize_session = False)
    db.session.delete(vacation)
    db.session.commit()
    return redirect(url_for('vacations'))



#                                                                                           ITINERARY INFORMATION

@app.route('/add_itinerary/<int:vacation_id>', methods = ['GET'])
def reroute_add_itinerary(vacation_id):
    print("rerouted!!!!")
    return render_template('add_itinerary.html', vacation_id = vacation_id)

@app.route('/add_itinerary_submit/<int:vacation_id>', methods=['POST'])
def add_itinerary(vacation_id):
    if(request.method == 'POST'):
        new_activity = request.form.get('activity')

        date_of_activity_str = request.form.get('date_of_activity')
        date_of_activity = datetime.strptime(date_of_activity_str, '%Y-%m-%d').date()

        cost_of_activity = request.form.get('cost_of_activity')
        new_itinerary = Itinerary(activity = new_activity, date_of_activity = date_of_activity, 
                                  cost_of_activity = cost_of_activity, vacation_id = vacation_id)
        print("Itinerary added!")
        db.session.add(new_itinerary)
        db.session.commit()
        return redirect(url_for('view_vacation', vacation_id=vacation_id))
    return redirect(url_for('vacations'))

@app.route('/delete_itinerary/<int:itinerary_id>', methods = ['POST'])
def delete_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    vacation_id = itinerary.vacation_id
    db.session.delete(itinerary)
    db.session.commit()
    return redirect(url_for('view_vacation', vacation_id = vacation_id))











    
'''
@app.route('/delete_all')
def delete_vacations():
    db.session.query(Vacation).delete()
    db.session.commit()
    return redirect(url_for('vacation'))
'''





#                                                                       LOGIN INFORMATION





if __name__ == '__main__':
    app.run(debug=True)