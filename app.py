from flask import Flask, request
from flask.json import jsonify
from server import app, db

from models import Customers

@app.route('/account-delete', methods=['GET', 'POST'])
def account_delete():
    data = {
        "message": "An error ocurred",
        "success": False,
    }

    if request.method == 'POST':

        try:
            customerid = int(request.form.get('customerid'))
        except ValueError:
            return jsonify(data), 400

        customer = Customers.query.get(customerid)
        
        if customer is None:
            return jsonify(data), 404

        customer.firstname = None
        customer.lastname = None
        customer.address1 = None
        customer.creditcardtype = None
        customer.creditcard = None
        customer.creditcardexpiration = None
        customer.username = None
        customer.password = None
        customer.deleted = 'Y'

        db.session.add(customer)
        db.session.commit()

        data.update(message="Deleted", success=True)
        return jsonify(data), 200
    return jsonify(data), 400


if __name__ == '__main__':
    from debugger import initialize_flask_server_debugger_if_needed
    
    initialize_flask_server_debugger_if_needed()
    app.run(host='0.0.0.0', port=5000)