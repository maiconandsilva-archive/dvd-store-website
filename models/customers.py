from server import db

customerhistory = db.Table('cust_hist',
    db.Column('customerid', db.Integer,
        db.ForeignKey('customers.customerid'), nullable=False),
    db.Column('orderid', db.Integer,
        db.ForeignKey('orders.orderid'), nullable=False),
    db.Column('prod_id', db.Integer,
        db.ForeignKey('products.prod_id'), nullable=False)
)

class Customers(db.Model):
    __tablename__ = 'customers'

    customerid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    address1 = db.Column(db.String(50))
    address2 = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip = db.Column(db.Integer)
    country = db.Column(db.String(50))
    region = db.Column(db.Integer)
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    creditcardtype = db.Column(db.Integer)
    creditcard = db.Column(db.String(50))
    creditcardexpiration = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    age = db.Column(db.Integer)
    income = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    deleted = db.Column(db.String(1), nullable=False, default='N')
    shopping_history = db.relationship('Orders', secondary='cust_hist')
    products_bought = db.relationship('Products', secondary='cust_hist')

class Orders(db.Model):
    """Tabela de pedidos"""

    __tablename__ = 'orders'

    orderid = db.Column(db.Integer, primary_key=True)
    orderdate = db.Column(db.DateTime, nullable=False)
    customerid = db.Column(db.Integer,
        db.ForeignKey('customers.customerid'), nullable=True)
    netamount = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    tax = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    totalamount  = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    customer = db.relationship('Customers')

class OrderLines(db.Model):
    """Tabela com os produtos por pedido"""

    __tablename__ = 'orderlines'

    orderlineid = db.Column(db.Integer, nullable=False)
    orderid = db.Column(db.Integer,
        db.ForeignKey('orders.orderid'), primary_key=True)
    prod_id = db.Column(db.Integer,
        db.ForeignKey('products.prod_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    orderdate = db.Column(db.DateTime, nullable=False)
    product = db.relationship('Products')
    orders = db.relationship('Orders')