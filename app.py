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
    customerid = None

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

        # data.update(message="Deleted", success=True)

        customer = Customers.query.get(customerid)
    else:
        return jsonify(data), 404
    return f"""
        <h1>Customer</h1>
        <ul>
            <li>Email: {customer.email}</li>
            <li>Genero: {customer.gender}</li>
            <li>Customerid: {customer.customerid}</li>
            <li>Firstname: {customer.firstname}</li>
            <li>Lastname: {customer.lastname}</li>
            <li>Address1: {customer.address1}</li>
            <li>Address2: {customer.address2}</li>
            <li>City: {customer.city}</li>
            <li>State: {customer.state}</li>
            <li>Zip: {customer.zip}</li>
            <li>Country: {customer.country}</li>
            <li>Region: {customer.region}</li>
            <li>Email: {customer.email}</li>
            <li>Phone: {customer.phone}</li>
            <li>Creditcardtype: {customer.creditcardtype}</li>
            <li>Creditcard: {customer.creditcard}</li>
            <li>Creditcardexpiration: {customer.creditcardexpiration}</li>
            <li>Username: {customer.username}</li>
            <li>Password: {customer.password}</li>
            <li>Age: {customer.age}</li>
            <li>Income: {customer.income}</li>
            <li>Gender: {customer.gender}</li>
        </ul>
    """


if __name__ == '__main__':
    from debugger import initialize_flask_server_debugger_if_needed
    
    initialize_flask_server_debugger_if_needed()
    app.run(host='0.0.0.0', port=5000)