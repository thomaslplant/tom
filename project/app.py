from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField

app = Flask(__name__)
db = SQLAlchemy(app)

# # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.77.106/CocktailBar"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['SQLALchemy_DATABASE_URI'] = "sqlite:///"
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

from application import routes

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


class CustomerTable(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)
    is_old_enough = db.Column(db.Boolean, nullable=False)

class CustomerForm(FlaskForm):
    name = StringField('Full Name')
    is_old_enough = BooleanField('Is over 18')
    submit = SubmitField('Enter Details')

@app.route('/customer', methods=['GET', 'POST'])
def add_customer():
    error = ""
    form = CustomerForm()

    if request.method == 'POST':
        name = form.name.data
        is_old_enough = form.is_old_enough.data
        

        if bool(is_old_enough) == False:
            error = "Customer must be 18 or over"
        else:
            if len(name) == 0:
                error = "Please fill in all fields"
            else:
                return  render_template('customer.html', form=form, message=error)
                
    person = CustomerTable(name=form.name.data, is_old_enough=form.is_old_enough.data)
    db.session.add(person)
    db.session.commit()
    customers = CustomerTable.query.all()

    return render_template('customer.html', form=form, message=error)
    
    


# class Customer_table(db.Model):
#     name = db.Column(db.String(30), nullable=False, primary_key=True)
#     is_old_enough = db.Column(db.Boolean, nullable=False)

# db.create_all

# @app.route('/customer', methods=['GET','POST'])
# def add_customer():
#     if request.form:
#         person = CustomerForm(name=request.form.get("name"), is_old_enough=request.form.get("18 or over"))
#         db.session.add(person)
#         db.session.commit()
#     registrees =Customer_table.query.all()
#     return render_template("home.html", registrees=registrees)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('home.html', title="Homepage")

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')