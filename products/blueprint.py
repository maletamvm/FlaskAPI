from flask import Blueprint
from flask import render_template

from models import Products

products = Blueprint('products', __name__, template_folder='templates')

@products.route('/')
def index():
    products=Products.query.all()
    return render_template('products/index.html',products=products)
