# THIRD PARTY IMPORTS
from flask.globals import g, request, session
from werkzeug.utils import redirect

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


@app.before_request
def upgrade_http_request():
    if app.config.get('FLASK_ENV') == 'production' and not request.is_secure:
        url = request.url.replace('http://', 'https://')
        return redirect(url, code=301)
    

@app.context_processor
def utility_processor():
    """Pass mask function to Jinja"""
    return dict(mask=mask)