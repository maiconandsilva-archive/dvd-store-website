from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config.from_object(os.environ.get('APPSETTINGS'))

db = SQLAlchemy(app)


@app.route('/test')
def test():
    from models import Customers
    from models import Orders
    from models import Products
    from models import Categories
    from models import Inventory
    from models import OrderLines
    from models import Orders
    from models import Reorder

    customer = Customers.query.filter_by(customerid=7888).one()
    order = Orders.query.filter_by(customerid=7888).limit(1)[0]
    # customer_shopping_history = customer.shopping_history.
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
        <li>Shopping_history: {customer.shopping_history}</li>
        <li>Products_bought: {customer.products_bought}</li>
    </ul>
    """


if __name__ == '__main__':
    from debugger import initialize_flask_server_debugger_if_needed
    
    initialize_flask_server_debugger_if_needed()
    app.run(host='0.0.0.0', port=5000)