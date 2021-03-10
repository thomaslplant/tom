from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.77.106/CocktailBar"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALchemy_DATABASE_URI'] = "sqlite:///"
app.config['SECRET_KEY'] = "TEST"

db = SQLAlchemy(app)

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    is_old_enough = db.Column(db.Boolean, nullable=False)
    

class Bartender(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    rate_of_pay = db.Column(db.Float, nullable=False)

class Drinks(db.Model):
    beverage_id = db.Column(db.Integer, primary_key=True)
    beverage_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    alcohol_percent = db.Column(db.Float, nullable=False)
    units_of_alcohol = db.Column(db.Float, nullable=False)

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    payment_type = db.Column(db.String(30), nullable=False)
    bank = db.Column(db.String(30), nullable=True)
    account_number = db.Column(db.Integer, nullable=True)
    sort_code = db.Column(db.Integer, nullable=True)
    cvv = db.Column(db.Integer, nullable=True)

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable = False)
    order_cost = db.Column(db.Float, nullable=False)
    datetime_of_order = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customer.customer_id'))
    beverage_id = db.Column('beverage_id', db.Integer, db.ForeignKey('drinks.beverage_id'))
    employee_id = db.Column('employee_id', db.Integer, db.ForeignKey('bartender.employee_id'))
    payment_id = db.Column('payment_id', db.Integer, db.ForeignKey('payment.payment_id'))




if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')