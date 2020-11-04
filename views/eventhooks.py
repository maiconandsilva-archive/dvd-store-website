# THIRD PARTY IMPORTS
from flask.globals import g, session

# LOCAL IMPORTS
from app import app
from helpers import mask
from models.customers import Customers


@app.before_request
def assign_loggedin_customer():
    g.user = None
    customerid = session.get('customerid')
    if customerid is not None:
        customer = Customers.query.get(customerid)
        if customer is not None and customer.is_active:
                g.user = customer
        else:
            session.clear()


@app.context_processor
def utility_processor():
    """Pass mask function to Jinja"""
    return dict(mask=mask)