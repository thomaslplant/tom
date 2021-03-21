from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import CustomerTable, BartenderTable, DrinksTable, PaymentTable, OrdersTable

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
    
        test1 = CustomerTable(first_name="Tom", last_name="Plant", is_old_enough=True)
        test2 = BartenderTable(name="Peter Wilson", start_date="2018-01-31", position="Team Leader", rate_of_pay=9.40)
        test3 = DrinksTable(beverage_name="Peroni", price=3.99, alcohol_percent=5.0, units_of_alcohol=1.7)
        test4 = PaymentTable(payment_type="Debit Card", bank="Barclays", account_number=18231723, sort_code=128374, cvv=987)
        
        db.session.add(test1)
        db.session.add(test2)
        db.session.add(test3)
        db.session.add(test4)
        db.session.commit()

        test5 = OrdersTable(quantity=1, order_cost=3.99, datetime_of_order="2021-03-10 15:13:30")

        db.session.add(test5)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# Customer Testing

class TestCustomer(TestBase):
    def test_add_customer(self):
        response = self.client.post(url_for('add_customer', customer_id=1),
            data = dict(first_name="Tom", last_name="Plant"), follow_redirects=True)
class TestUpdateCustomer(TestBase):
    def test_update_customer(self):
        response = self.client.post(url_for('update_customer', customer_id=1),
            data = dict(first_name="Tom", last_name="Plant"), follow_redirects=True)
class TestDeleteCustomer(TestBase):
    def test_delete_customer(self):
        response = self.client.get(url_for('delete_customer', customer_id=1), follow_redirects=True)
        assert b"Tom", response.data
# Bartender Testing

class TestBartender(TestBase):
    def test_add_bartender(self):
        response = self.client.post(url_for('add_bartender', employee_id=1),
            data = dict(name="Peter Wilson", start_date="21/01/2019", position="Team Leader", rate_of_pay=9.45), follow_redirects=True)
class TestUpdateBartender(TestBase):
    def test_update_bartender(self):
        response = self.client.post(url_for('update_bartender', employee_id=1),
            data = dict(name="Peter Wilson", start_date="21/01/2019", position="Team Leader", rate_of_pay=9.45), follow_redirects=True)
class TestDeleteBartender(TestBase):
    def test_delete_bartender(self):
        response = self.client.get(url_for('delete_bartender', employee_id=1), follow_redirects=True)
        assert b"Peter Wilson", response.data

# Drinks Testing

class TestDrinks(TestBase):
    def test_add_drink(self):
        response = self.client.post(url_for('add_drink', beverage_id=1),
            data = dict(beverage_name="Peroni", price=3.95, alcohol_percent=5.1, units_of_alcohol=1.5), follow_redirects=True)
class TestUpdateDrinks(TestBase):
    def test_update_drink(self):
        response = self.client.post(url_for('update_drink', beverage_id=1),
            data = dict(beverage_name="Peroni", price=3.95, alcohol_percent=5.1, units_of_alcohol=1.5), follow_redirects=True)
class TestDeleteDrink(TestBase):
    def test_delete_drink(self):
        response = self.client.get(url_for('delete_drink', beverage_id=1), follow_redirects=True)
        assert b"Peroni", response.data

# Payment Testing

class TestPayment(TestBase):
    def test_add_payment(self):
        response = self.client.post(url_for('add_payment', payment_id=1),
            data = dict(payment_type="Debit Card", bank="Santander", account_number=12237198, sort_code=712332, cvv=678), follow_redirects=True)
class TestUpdatePayment(TestBase):
    def test_update_payment(self):
        response = self.client.post(url_for('update_payment', payment_id=1),
            data = dict(payment_type="Debit Card", bank="Santander", account_number=12237198, sort_code=712332, cvv=678), follow_redirects=True)
class TestDeletePayment(TestBase):
    def test_delete_payment(self):
        response = self.client.get(url_for('delete_payment', payment_id=1), follow_redirects=True)
        assert b"Debit Card", response.data
# Orders Testing

class TestOrders(TestBase):
    def test_add_orders(self):
        response = self.client.post(url_for('add_orders', order_id=1),
            data = dict(quantity=1, order_cost=3.95, datetime_of_order="16/03/2021 19:21:49"), follow_redirects=True)
class TestUpdateOrders(TestBase):
    def test_update_orders(self):
        response = self.client.post(url_for('update_orders', order_id=1),
            data = dict(quantity=1, order_cost=3.95, datetime_of_order="16/03/2021 19:21:49"), follow_redirects=True)
class TestDeleteOrder(TestBase):
    def test_delete_order(self):
        response = self.client.get(url_for('delete_orders', order_id=1), follow_redirects=True)
        assert b"1", response.data

class TestReturnTemplate(TestBase):
    def create_app(self):
        return app
    def test_return_template1(self):
        self.client.get('/')
        self.assert_template_used('home.html')
        self.assert_context("title", "Homepage")

    def test_return_template2(self):
        self.client.get('/customer/view')
        self.assert_template_used('customerview.html')
        self.assert_context("title", "Customer View")
    
    def test_return_template3(self):
        self.client.get('/bartender/view')
        self.assert_template_used('bartenderview.html')
        self.assert_context("title", "Bartender View")

    def test_return_template4(self):
        self.client.get('/drinks/view')
        self.assert_template_used('drinksview.html')
        self.assert_context("title", "Drinks View")

    def test_return_template5(self):
        self.client.get('/payment/view')
        self.assert_template_used('paymentview.html')
        self.assert_context("title", "Payment View")

    def test_return_template6(self):
        self.client.get('/orders/view')
        self.assert_template_used('ordersview.html')
        self.assert_context("title", "Orders View")