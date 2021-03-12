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

    def start_test(self):
        db.create_all()

        test1 = Customer(name="Jeff Brown", is_old_enough=True)
        test2 = Bartender(name="Peter Wilson", start_date="2018-01-31", position="Team Leader", rate_of_pay=9.40)
        test3 = Drinks(beverage_name="Peroni", price=3.99, alcohol_percent=5.0, units_of_alcohol=1.7)
        test4 = Payment(payment_type="Debit Card", bank="Barclays", account_number=18231723, sort_code=128374, cvv=987)

        db.session.add(test1)
        db.session.add(test2)
        db.session.add(test3)
        db.session.add(test4)
        db.session.commit()

        test5 = Orders(quantity=1, order_cost=3.99, datetime_of_order="2021-03-10 15:13:30", customer_id=1, beverage_id=1, employee_id=1, payment_id=1)

        db.session.add(test5)
        db.session.commit()

    def end_test(self):
        db.session.remove()
        db.drop_all()