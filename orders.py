from flask import request, jsonify
from app import app, db
from models import Order, OrderProduct
from datetime import datetime

# Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    # getting the request data
    data = request.get_json()
    # getting the user id from the request data
    order = Order(customer_id=data['customer_id'], order_date=datetime.now())
    db.session.add(order)
    db.session.commit()
    # Create Order product for each product in the order
    for product_id, quantity in data['products'].items():
        order_product = OrderProduct(order_id=order.id, product_id=product_id, quantity=quantity)
        db.session.add(order_product)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201

# Get an order ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    # if the order is not found, 404 error
    if order is None:
        return jsonify({'message': 'Order not found'}), 404
    return jsonify({'customer_id': order.customer_id, 'order_date': order.order_date, 'products': [{'product_id': op.product_id, 'quantity': op.quantity} for op in order.products]})

# Update an order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get(order_id)
    #If the order is not found, 404 error
    if order is None:
        return jsonify({'message': 'Order not found'}), 404
    data = request.get_json()
    # Updates the order details
    order.customer_id = data['customer_id']
    order.order_date = datetime.now()
    db.session.commit()
    for product_id, quantity in data['products'].items():
        order_product = OrderProduct.query.filter_by(order_id=order.id, product_id=product_id).first()
        if order_product:
            order_product.quantity = quantity
        else:
            order_product = OrderProduct(order_id=order.id, product_id=product_id, quantity=quantity)
            db.session.add(order_product)
    db.session.commit()
    return jsonify({'message': 'Order updated successfully'})

#Deletes an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({'message': 'Order not found'}), 404
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'})

# Get a list of all orders
@app.route('/orders', methods=['GET'])
def list_orders():
    orders = Order.query.all()
    return jsonify([{'id': order.id, 'customer_id': order.customer_id, 'order_date': order.order_date} for order in orders])