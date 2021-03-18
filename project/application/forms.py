from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FloatField, IntegerField

class CustomerForm(FlaskForm):
    first_name = StringField('First Name ')
    last_name = StringField('Last Name ')
    is_old_enough = BooleanField('Is over 18')
    submit = SubmitField('Enter Details')

class BartenderForm(FlaskForm):
    name = StringField('Full name')
    start_date = StringField('Start date')
    position = StringField('Position    ')
    rate_of_pay = FloatField('Hourly pay')
    submit = SubmitField('Enter details')

class DrinksForm(FlaskForm):
    beverage_name = StringField('Name of Drink')
    price = FloatField('Price')
    alcohol_percent = FloatField('Percentage')
    units_of_alcohol = FloatField('Units')
    submit = SubmitField('Enter details')

class PaymentForm(FlaskForm):
    payment_type = StringField('Payment Type')
    bank = StringField('Bank')
    account_number = IntegerField('Account Number')
    sort_code = IntegerField('Sort Code')
    cvv = IntegerField('CVV')
    submit = SubmitField('Enter payment details')

class OrdersForm(FlaskForm):
    quantity = IntegerField('How many Items')
    order_cost = FloatField('Total order cost')
    datetime_of_order = StringField('Date and Time of order')
    submit = SubmitField('Enter Order details')