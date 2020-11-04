from flask.globals import g
from app import app, db

from views import *

from helpers import mask


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
 
# TODO: for sprint-4. To be refactored
@app.context_processor
def utility_processor():
    """Pass mask function to jinja"""
    return dict(mask=mask)


app.add_url_rule('/signin', view_func=Signin.as_view('signin'))
app.add_url_rule('/signup', view_func=Signup.as_view('signup'))
app.add_url_rule('/account', view_func=AccountView.as_view('account'))
app.add_url_rule('/account/signout', view_func=Signout.as_view('signout'))
app.add_url_rule('/account/delete', view_func=AccountDelete.as_view('account-delete'))

if __name__ == '__main__':
    from debugger import initialize_flask_server_debugger_if_needed
    
    initialize_flask_server_debugger_if_needed()
    app.run(host='0.0.0.0', port=5000)