from flask import render_template , Blueprint
from API.products.forms import ProductForm

product=Blueprint('products',__name__)


@product.route('/create')
def create_product():
    form =ProductForm()
    return render_template('product/create_product.html',form=form)