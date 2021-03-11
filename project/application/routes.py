# from app import app, db
# from wtforms import StringField, BooleanField
# from flask_wtf import FlaskForm
# from flask import Flask, render_template, request
# from application.models import CustomerForm

# @app.route('/', methods=['GET', 'POST'])
# def homepage():
#     return render_template('home.html', title="Homepage")

# @app.route('/customer', methods=['GET', 'POST'])
# def add_customer():
#     error = ""
#     form = CustomerForm()

#     if request.method == 'POST':
#         name = form.name.data
#         is_old_enough = form.is_old_enough.data
#         if bool(is_old_enough) == False:
#             error = "Customer must be 18 or over"
#         else:
#             if len(name) == 0:
#                 error = "Please fill in all fields"
#             else:
#                 return "Thank You! Return to Customer page"
#     return render_template('customer.html', form=form, message=error)


# if __name__=='__main__':
#     app.run(debug=True, host='0.0.0.0')