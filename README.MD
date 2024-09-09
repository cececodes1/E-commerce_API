E-commerce API

Overview

This is a RESTful API built with Flask that provides a comprehensive e-commerce platform for managing products. The API uses Flask-SQLAlchemy to interact with a MySQL database.

Features

- Create, Read, Update, and Delete (CRUD) endpoints for managing products
- Capture essential product details, including product name and price
- List all available products in the e-commerce platform

API Endpoints

Create a Product

POST /products
- Request Body: JSON object with name and price fields
- Response: JSON object with a success message and a 201 status code
- Error Handling: Returns a 400 status code with an error message if the request body is invalid

Get a Product
GET /products/:id

- Path Parameter: id (integer)
- Response: JSON object with the product's name and price fields
- Error Handling: Returns a 404 status code with an error message if the product is not found

Update a Product
PUT /products/:id

- Path Parameter: id (integer)
- Request Body: JSON object with name and price fields
- Response: JSON object with a success message
- Error Handling: Returns a 404 status code with an error message if the product is not found

Delete a Product
DELETE /products/:id

- Path Parameter: id (integer)
- Response: JSON object with a success message
- Error Handling: Returns a 404 status code with an error message if the product is not found

List All Products
GET /products

- Response: JSON array of objects with each product's id, name, and price fields

Database Integration

- Utilizes Flask-SQLAlchemy to integrate a MySQL database into the application
- Designs and creates necessary models to represent products

Data Validation and Error Handling

- Implements data validation mechanisms to ensure user inputs meet specified criteria

- Uses try, except, else, and finally blocks to handle errors gracefully and provide informative error messages

Getting Started

- Clone the repository: git clone https://github.com/cececodes1/E-commerce_API.git
- Install the dependencies: pip install -r requirements.txt
- Run the application: python app.py
