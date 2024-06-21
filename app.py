# Config
from flask import Flask
app = Flask(__name__)

# Routes

# Index Route
@app.route('/')
def index():
	return "Hello, this is PetFax!"

# Pets Index Route
@app.route('/pets')
def pets():
	return 'These are our pets available for adoption!'