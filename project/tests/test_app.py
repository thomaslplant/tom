from flask import url_for
from flask_testing import TestCase
from app import app, db, Customer, Bartender, Drinks, Payment, Orders

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()

        sample1 = Customer(name="Jeff Brown", is_old_enough=True)
        sample2 = Bartender(name="Peter Wilson", start_date="2018-01-31", position="Team Leader", rate_of_pay=9.40)
        sample3 = Drinks(beverage_name="Peroni", price=3.99, alcohol_percent=5.0, units_of_alcohol=1.7)
        sample4 = Payment(payment_type="Debit Card", bank="Barclays", account_number=18231723, sort_code=128374, cvv=987)

        db.session.add(sample1)
        db.session.add(sample2)
        db.session.add(sample3)
        db.session.add(sample4)
        db.session.commit()

        sample5 = Orders(quantity=1, order_cost=3.99, datetime_of_order="2021-03-10 15:13:30", customer_id=1, beverage_id=1, employee_id=1, payment_id=1)

        db.session.add(sample5)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()