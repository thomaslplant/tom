from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALchemy_DATABASE_URI'] = "sqlite:///"
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    is_old_enough = db.Column(db.Boolean, nullable=False)

class CustomerTable(FlaskForm):
    name = StringField('Full Name')
    is_old_enough = BooleanField('Is over 18')
    submit = SubmitField('Enter Details')

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('home.html', title="Homepage")

@app.route('/customer', methods=['GET', 'POST'])
def add_customer():
    form = CustomerTable
    name = form.name.data
    is_old_enough = form.is_old_enough.data
    person = CustomerTable(name=form.name.data, is_old_enough=form.is_old_enough.data)
    db.session.add(person)
    db.session.commit()
    return f"Customer('{add_customer.person}')"






if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')