from flask import Flask, redirect, render_template, request, flash
from application import app, db

class CustomerTable(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    is_old_enough = db.Column(db.Boolean, nullable=False)

class BartenderTable(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.String(11), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    rate_of_pay = db.Column(db.Float, nullable=False)

class DrinksTable(db.Model):
    beverage_id = db.Column(db.Integer, primary_key=True)
    beverage_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    alcohol_percent = db.Column(db.Float, nullable=False)
    units_of_alcohol = db.Column(db.Float, nullable=False)

class PaymentTable(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    payment_type = db.Column(db.String(30), nullable=False)
    bank = db.Column(db.String(30), nullable=True)
    account_number = db.Column(db.Integer, nullable=True)
    sort_code = db.Column(db.Integer, nullable=True)
    cvv = db.Column(db.Integer, nullable=True)

class OrdersTable(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable = False)
    order_cost = db.Column(db.Float, nullable=False)
    datetime_of_order = db.Column(db.String(25), nullable=False)
