from wtforms import StringField, SubmitField, BooleanField
from flask_wtf import FlaskForm

class CustomerForm(FlaskForm):
    name = StringField('Full Name')
    is_old_enough = BooleanField('True or False')
    submit = SubmitField('Enter Details')
