from app import app, db
from flask import request, jsonify
from models import Product
from sqlalchemy.exc import SQLAlchemyError



#Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        if 'name' not in data or 'price' not in data:
            return jsonify({'error': 'Invalid JSON payload. Missing "name" or "price" field.'}), 400
        product = Product(name=data['name'], price=data['price'])
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'}), 201
    except SQLAlchemyError:
        return jsonify({'error': 'Failed to create product. Please try again later.'}), 500

# Get a product ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({'error': 'Product with ID {} not found'}), 404
        return jsonify({'name': product.name, 'price': product.price})
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error: {}'.format(e)}), 500

#Update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'message': 'Product not found'}), 404
    data = request.get_json()
    product.name = data['name']
    product.price = data['price']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

#Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'message': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

#Get a list of all products
@app.route('/products', methods=['GET'])
def list_products():
    products = Product.query.all()
    return jsonify([{'id': product.id, 'name': product.name, 'price': product.price} for product in products])