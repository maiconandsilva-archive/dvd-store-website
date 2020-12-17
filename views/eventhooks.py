# THIRD PARTY IMPORTS
from models.isolated.customer_personal_info import CustomerPersonalInfo
from flask.globals import g, request, session
from werkzeug.utils import redirect

# LOCAL IMPORTS
from app import app
from helpers import mask
from models.customers import Customers


@app.before_request
def assign_loggedin_customer():
    g.user = None
    g.allowdecryption = True
    
    customerid = session.get('customerid')
    if customerid is not None:
        customer = CustomerPersonalInfo.query.get(customerid)
        if customer is not None and customer.more.is_active:
                g.user = customer
        else:
            session.clear()    

@app.context_processor
def utility_processor():
    """Pass mask function to Jinja"""
    return dict(mask=mask)