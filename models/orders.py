from app import db
import models.products as mp


customerhistory = db.Table('cust_hist',
    db.Column('customerid', db.Integer,
        db.ForeignKey('customers.customerid'), nullable=False),
    db.Column('orderid', db.Integer,
        db.ForeignKey('orders.orderid'), nullable=False),
    db.Column('prod_id', db.Integer,
        db.ForeignKey('products.prod_id'), nullable=False)
)


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
    products = db.relationship(mp.Products, secondary='cust_hist')


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
    product = db.relationship(mp.Products)
    orders = db.relationship('Orders')