from app import db

class Customers(db.Model):
    __tablename__ = 'customers'

    customerid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    address1 = db.Column(db.String(50), nullable=False)
    address2 = db.Column(db.String(50))
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50))
    zip = db.Column(db.Integer)
    country = db.Column(db.String(50), nullable=False)
    region = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    creditcardtype = db.Column(db.Integer, nullable=False)
    creditcard = db.Column(db.String(50), nullable=False)
    creditcardexpiration = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    income = db.Column(db.Integer)
    gender = db.Column(db.String(50))

class CustomerHistory(db.Model):
    __tablename__ = 'cust_hist'
    __table_args__ = (
        db.PrimaryKeyConstraint('customerid', 'orderid', 'prod_id'),
    )

    customerid = db.Column(
        db.Integer, db.ForeignKey('cust_hist.customerid'), nullable=False)
    orderid = db.Column(db.Integer, nullable=False)
    prod_id = db.Column(db.Integer, nullable=False)

class Orders(db.Model):
    __tablename__ = 'orders'

    orderid = db.Column(db.Integer, primary_key=True)
    orderdate = db.Column(db.DateTime, nullable=False)
    customerid = db.Column(db.Integer, db.ForeignKey('cust_hist.customerid'))
    netamount = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    tax = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    totalamount  = db.Column(db.Numeric(precision=12, scale=2), nullable=False)

class OrderLines(db.Model):
    __tablename__ = 'orderlines'

    orderlineid = db.Column(db.Integer, primary_key=True)
    orderid = db.Column(
        db.Integer, db.ForeignKey('orders.orderid'), nullable=False)
    prod_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    orderdate = db.Column(db.DateTime, nullable=False)
