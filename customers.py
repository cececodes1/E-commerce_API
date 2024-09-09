from app import app, db
from models import Customer, CustomerAccount

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = Customer(name=data['name'], email=data['email'], phone_number=data['phone_number'])
    db.session.add(customer)
    db.session.commit()
    return jsonify({'message': 'Customer created successfully'}), 201

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        return jsonify({'message': 'Customer not found'}), 404
    return jsonify({'name': customer.name, 'email': customer.email, 'phone_number': customer.phone_number})

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        return jsonify({'message': 'Customer not found'}), 404
    data = request.get_json()
    customer.name = data['name']
    customer.email = data['email']
    customer.phone_number = data['phone_number']
    db.session.commit()
    return jsonify({'message': 'Customer updated successfully'})

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        return jsonify({'message': 'Customer not found'}), 404
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully'})

@app.route('/customer-accounts', methods=['POST'])
def create_customer_account():
    data = request.get_json()
    customer_account = CustomerAccount(customer_id=data['customer_id'], username=data['username'], password=data['password'])
    db.session.add(customer_account)
    db.session.commit()
    return jsonify({'message': 'Customer account created successfully'}), 201

@app.route('/customer-accounts/<int:customer_account_id>', methods=['GET'])
def get_customer_account(customer_account_id):
    customer_account = CustomerAccount.query.get(customer_account_id)
    if customer_account is None:
        return jsonify({'message': 'Customer account not found'}), 404
    return jsonify({'username': customer_account.username, 'customer_id': customer_account.customer_id})

@app.route('/customer-accounts/<int:customer_account_id>', methods=['PUT'])
def update_customer_account(customer_account_id):
    customer_account = CustomerAccount.query.get(customer_account_id)
    if customer_account is None:
        return jsonify({'message': 'Customer account not found'}), 404
    data = request.get_json()
    customer_account.username = data['username']
    customer_account.password = data['password']
    db.session.commit()
    return jsonify({'message': 'Customer account updated successfully'})

@app.route('/customer-accounts/<int:customer_account_id>', methods=['DELETE'])
def delete_customer_account(customer_account_id):
    customer_account = CustomerAccount.query.get(customer_account_id)
    if customer_account is None:
        return jsonify({'message': 'Customer account not found'}), 404
    db.session.delete(customer_account)
    db.session.commit()
    return jsonify({'message': 'Customer account deleted successfully'})