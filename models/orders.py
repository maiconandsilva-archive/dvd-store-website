# THIRD PARTY IMPORTS 
from sqlalchemy.orm import backref

# LOCAL IMPORTS
from app import db
import models.products as mp


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
    details = db.relationship('OrderLines', backref='payment')


class OrderLines(db.Model):
    """Tabela com os produtos por pedido"""

    __tablename__ = 'orderlines'

    orderlineid = db.Column(db.Integer, primary_key=True)
    orderid = db.Column(db.Integer,
        db.ForeignKey('orders.orderid'), primary_key=True)
    prod_id = db.Column(db.Integer,
        db.ForeignKey('products.prod_id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    product = db.relationship(mp.Products)
    orders = db.relationship('Orders')

