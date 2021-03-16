from flask import Flask, redirect, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateField, FloatField

app = Flask(__name__)
db = SQLAlchemy(app)

# # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.77.106/CocktailBar"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALchemy_DATABASE_URI'] = "sqlite:///data.db"
# app.config['SECRET_KEY'] = "TEST"


# class Customer(db.Model):
#     customer_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     is_old_enough = db.Column(db.Boolean, nullable=False)
    

# class Bartender(db.Model):
#     employee_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     start_date = db.Column(db.Date, nullable=False)
#     position = db.Column(db.String(50), nullable=False)
#     rate_of_pay = db.Column(db.Float, nullable=False)

# class Drinks(db.Model):
#     beverage_id = db.Column(db.Integer, primary_key=True)
#     beverage_name = db.Column(db.String(50), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     alcohol_percent = db.Column(db.Float, nullable=False)
#     units_of_alcohol = db.Column(db.Float, nullable=False)

# class Payment(db.Model):
#     payment_id = db.Column(db.Integer, primary_key=True)
#     payment_type = db.Column(db.String(30), nullable=False)
#     bank = db.Column(db.String(30), nullable=True)
#     account_number = db.Column(db.Integer, nullable=True)
#     sort_code = db.Column(db.Integer, nullable=True)
#     cvv = db.Column(db.Integer, nullable=True)

# class Orders(db.Model):
#     order_id = db.Column(db.Integer, primary_key=True)
#     quantity = db.Column(db.Integer, nullable = False)
#     order_cost = db.Column(db.Float, nullable=False)
#     datetime_of_order = db.Column(db.DateTime, nullable=False)
#     customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customer.customer_id'))
#     beverage_id = db.Column('beverage_id', db.Integer, db.ForeignKey('drinks.beverage_id'))
#     employee_id = db.Column('employee_id', db.Integer, db.ForeignKey('bartender.employee_id'))
#     payment_id = db.Column('payment_id', db.Integer, db.ForeignKey('payment.payment_id'))

# from application import routes

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


class CustomerTable(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    is_old_enough = db.Column(db.Boolean, nullable=False)

class CustomerForm(FlaskForm):
    first_name = StringField('First Name ')
    last_name = StringField('Last Name ')
    is_old_enough = BooleanField('Is over 18')
    submit = SubmitField('Enter Details')

class Bartender(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    rate_of_pay = db.Column(db.Float, nullable=False)

class BartenderForm(FlaskForm):
    name = StringField('Employee name')
    start_date = DateField('Start date')
    position = StringField('Employee position')
    rate_of_pay = FloatField('Hourly pay')
    submit = SubmitField('Enter details')

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('home.html', title="Homepage")

@app.route('/bartender', methods=['GET', 'POST'])
def add_bartender():
    return render_template('bartender.html', title="Bartender")

@app.route('/customer/view', methods=['GET', 'POST'])
def customer_view():
    return render_template('customerview.html', title="Customer View")

@app.route('/customer', methods=['GET', 'POST'])
def add_customer():
    error = ""
    form = CustomerForm()
    all_customers = CustomerTable.query.all()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        is_old_enough = form.is_old_enough.data
        person = CustomerTable(first_name=form.first_name.data, last_name=form.last_name.data, is_old_enough=form.is_old_enough.data )
        
        if len(first_name) == 0:
            error = "Please enter your first name"
        elif len(last_name) == 0:
            error = "Please enter your last name"
        elif bool(is_old_enough) == False:
            error = "Not old enough"
        else:
            db.session.add(person)
            db.session.commit()
            return render_template('customerview.html', all_customers=all_customers, form=form, message=error, title="Add Customer")


    return render_template('customer.html', all_customers=all_customers, form=form, message=error)

@app.route('/customer/update/<int:customer_id>', methods=['POST', 'GET'])
def update_customer(customer_id):
    customer_to_update = CustomerTable.query.get_or_404(customer_id)
    form = CustomerForm()
    if request.method == 'POST':
        customer_to_update.first_name = request.form["first_name"]
        customer_to_update.last_name = request.form["last_name"]
        try:
            db.session.commit()
            return redirect('/customer')
        except:
            return "Update Unsuccessful"
    else:
        return render_template('customerupdate.html', customer_to_update=customer_to_update)


db.create_all()


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')