from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://ecommerce_user:password@localhost/ecommerce_db"
db = SQLAlchemy(app)