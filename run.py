from app import app
from models import Customers

@app.route('/')
def main():
    customer = Customers.query.filter_by(customerid=1).one()
    return f'<h1>{customer.email}{customer.gender}<\h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)