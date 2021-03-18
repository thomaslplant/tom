from flask import Flask, redirect, render_template, request, flash, url_for
from application import app, db
from application.models import CustomerTable, BartenderTable, DrinksTable, PaymentTable, OrdersTable
from application.forms import CustomerForm, BartenderForm, DrinksForm,PaymentForm, OrdersForm

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('home.html', title="Homepage")

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

@app.route('/customer/delete/<int:customer_id>')
def delete_customer(customer_id):
    customer_to_delete = CustomerTable.query.get_or_404(customer_id)

    try:
        db.session.delete(customer_to_delete)
        db.session.commit()
        return redirect('/customer')
    except:
        return "The Customer couldn't be deleted!"


@app.route('/bartender/view', methods=['GET', 'POST'])
def view_bartender():
    return render_template('bartenderview.html', title="Bartender View")

@app.route('/bartender', methods=['GET', 'POST'])
def add_bartender():
    error = ""
    form = BartenderForm()
    all_bartenders = BartenderTable.query.all()
    if request.method == 'POST':
        name = form.name.data
        start_date = form.start_date.data
        position = form.position.data
        rate_of_pay = form.rate_of_pay.data
        employee = BartenderTable(name=form.name.data, start_date=form.start_date.data, position=form.position.data, rate_of_pay=form.rate_of_pay.data)
        
        if len(name) == 0:
            error = "Please enter your full name"
        elif len(start_date) < 10:
            error = "Please enter full date (DD/MM/YYYY)"
        elif len(position) == 0:
            error = "Please enter your position/job title"
        elif float(rate_of_pay) <= 0.00:
            error = "Please enter your hourly pay"
        else:
            db.session.add(employee)
            db.session.commit()
            return render_template('bartenderview.html', all_bartenders=all_bartenders, form=form, message=error, title="Add Bartender")

    return render_template('bartender.html', all_bartenders=all_bartenders, form=form, message=error)

@app.route('/bartender/update/<int:employee_id>', methods=['POST', 'GET'])
def update_bartender(employee_id):
    bartender_to_update = BartenderTable.query.get_or_404(employee_id)
    form = BartenderForm()
    if request.method == 'POST':
        bartender_to_update.name = request.form["name"]
        bartender_to_update.start_date = request.form["start_date"]
        bartender_to_update.position = request.form["position"]
        bartender_to_update.rate_of_pay = request.form["rate_of_pay"]
        try:
            db.session.commit()
            return redirect('/bartender')
        except:
            return "Bartender Update Unsuccessful"
    else:
        return render_template('bartenderupdate.html', bartender_to_update=bartender_to_update)

@app.route('/bartender/delete/<int:employee_id>')
def delete_bartender(employee_id):
    bartender_to_delete = BartenderTable.query.get_or_404(employee_id)

    try:
        db.session.delete(bartender_to_delete)
        db.session.commit()
        return redirect('/bartender')
    except:
        return "The Bartender couldn't be deleted!"

@app.route('/drinks/view', methods=['GET', 'POST'])
def drinks_view():
    return render_template('drinksview.html', title="Drinks View")

@app.route('/drinks', methods=['GET', 'POST'])
def add_drink():
    error = ""
    form = DrinksForm()
    all_drinks = DrinksTable.query.all()
    if request.method == 'POST':
        beverage_name = form.beverage_name.data
        price = form.price.data
        alcohol_percent = form.alcohol_percent.data
        units_of_alcohol = form.units_of_alcohol.data
        drink = DrinksTable(beverage_name=form.beverage_name.data, price=form.price.data, alcohol_percent=form.alcohol_percent.data, units_of_alcohol=form.units_of_alcohol.data)
        
        if len(beverage_name) == 0:
            error = "Please enter the name of the drink"
        elif float(price) <= 0.00:
            error = "Please enter the price of the drink"
        elif float(alcohol_percent) <= 0.00:
            error = "Please enter the alcohol percentage"
        elif float(units_of_alcohol) <= 0.00:
            error = "Please enter the the units of alcohol"
        else:
            db.session.add(drink)
            db.session.commit()
            return render_template('drinksview.html', all_drinks=all_drinks, form=form, message=error, title="Add Drinks")


    return render_template('drinks.html', all_drinks=all_drinks, form=form, message=error)

@app.route('/drinks/update/<int:beverage_id>', methods=['POST', 'GET'])
def update_drink(beverage_id):
    drink_to_update = DrinksTable.query.get_or_404(beverage_id)
    form = DrinksForm()
    if request.method == 'POST':
        drink_to_update.beverage_name = request.form["beverage_name"]
        drink_to_update.price = request.form["price"]
        drink_to_update.alcohol_percent = request.form["alcohol_percent"]
        drink_to_update.units_of_alcohol = request.form["units_of_alcohol"]
        try:
            db.session.commit()
            return redirect('/drinks')
        except:
            return "Update Unsuccessful"
    else:
        return render_template('drinksupdate.html', drink_to_update=drink_to_update)

@app.route('/drinks/delete/<int:beverage_id>')
def delete_drink(beverage_id):
    drink_to_delete = DrinksTable.query.get_or_404(beverage_id)

    try:
        db.session.delete(drink_to_delete)
        db.session.commit()
        return redirect('/drinks')
    except:
        return "The Drink couldn't be deleted!"

@app.route('/payment/view', methods=['GET', 'POST'])
def payment_view():
    return render_template('paymentview.html', title="Payment View")

@app.route('/payment', methods=['GET', 'POST'])
def add_payment():
    error = ""
    form = PaymentForm()
    all_payments = PaymentTable.query.all()
    if request.method == 'POST':
        payment_type = form.payment_type.data
        bank = form.bank.data
        account_number = form.account_number.data
        sort_code = form.sort_code.data
        cvv = form.cvv.data
        payment_method = PaymentTable(payment_type=form.payment_type.data, bank=form.bank.data, account_number=form.account_number.data, sort_code=form.sort_code.data, cvv=form.cvv.data)
        
        if payment_type == "Cash":
            db.session.add(payment_method)
            db.session.commit()
            return render_template('paymentview.html', all_payments=all_payments, form=form, message=error, title="Add Payment")
        else:
            if len(payment_type) == 0:
                error = "Please enter the payment type"
            elif len(bank) == 0:
                error = "Please enter the bank name"
            elif int(account_number) <= 9999999:
                error = "Account number needs to be 8 digits"
            elif int(sort_code) <= 99999:
                error = "Sort code needs to be 6 digits"
            elif int(cvv) <= 99:
                error = "Please enter the CVV"
            else:
                db.session.add(payment_method)
                db.session.commit()
                return render_template('paymentview.html', all_payments=all_payments, form=form, message=error, title="Add Payment")


    return render_template('payment.html', all_payments=all_payments, form=form, message=error)

@app.route('/payment/update/<int:payment_id>', methods=['POST', 'GET'])
def update_payment(payment_id):
    payment_to_update = PaymentTable.query.get_or_404(payment_id)
    form = PaymentForm()
    if request.method == 'POST':
        payment_to_update.payment_type = request.form["payment_type"]
        payment_to_update.bank = request.form["bank"]
        payment_to_update.account_number = request.form["account_number"]
        payment_to_update.sort_code = request.form["sort_code"]
        payment_to_update.cvv = request.form["cvv"]
        try:
            db.session.commit()
            return redirect('/payment')
        except:
            return "Update Unsuccessful"
    else:
        return render_template('paymentupdate.html', payment_to_update=payment_to_update)

@app.route('/payment/delete/<int:payment_id>')
def delete_payment(payment_id):
    payment_to_delete = PaymentTable.query.get_or_404(payment_id)

    try:
        db.session.delete(payment_to_delete)
        db.session.commit()
        return redirect('/customer')
    except:
        return "The Payment couldn't be deleted!"

@app.route('/orders/view', methods=['GET', 'POST'])
def orders_view():
    return render_template('ordersview.html', title="Orders View")

@app.route('/orders', methods=['GET', 'POST'])
def add_orders():
    error = ""
    form = OrdersForm()
    all_orders = OrdersTable.query.all()
    if request.method == 'POST':
        quantity = form.quantity.data
        order_cost = form.order_cost.data
        datetime_of_order = form.datetime_of_order.data
        # customer_id = form.customer_id.data
        whole_order = OrdersTable(quantity=form.quantity.data, order_cost=form.order_cost.data, datetime_of_order=form.datetime_of_order.data)#, customer_id=form.customer_id.data)
        
        if int(quantity) <= 0:
            error = "Please enter your first name"
        elif float(order_cost) == 0:
            error = "Please enter your last name"
        elif len(datetime_of_order) < 19:
            error = "Please enter Date and Time (DD/MM/YYYY HH:MM:SS)"
        else:
            db.session.add(whole_order)
            db.session.commit()
            return render_template('ordersview.html', all_orders=all_orders, form=form, message=error, title="Add Orders")

    return render_template('orders.html', all_orders=all_orders, form=form, message=error)

@app.route('/orders/update/<int:order_id>', methods=['POST', 'GET'])
def update_orders(order_id):
    order_to_update = OrdersTable.query.get_or_404(order_id)
    form = OrdersForm()
    if request.method == 'POST':
        order_to_update.quantity = request.form["quantity"]
        order_to_update.order_cost = request.form["order_cost"]
        order_to_update.datetime_of_order = request.form["datetime_of_order"]
        # order_to_update.customer_id = request.form["customer_id"]
        try:
            db.session.commit()
            return redirect('/orders')
        except:
            return "Update to Orders Unsuccessful"
    else:
        return render_template('ordersupdate.html', order_to_update=order_to_update)

@app.route('/orders/delete/<int:order_id>')
def delete_orders(order_id):
    order_to_delete = OrdersTable.query.get_or_404(order_id)

    try:
        db.session.delete(order_to_delete)
        db.session.commit()
        return redirect('/orders')
    except:
        return "The Order couldn't be deleted!"