from flask import Blueprint
from flask import render_template
from products.forms import ProductForm

from models import Products

from flask import request
from app import db
from flask import redirect
from flask import url_for

from flask import jsonify

from flask_security import login_required

products = Blueprint('product', __name__, template_folder='templates')


@products.route('/create',methods=['POST','GET'])
@login_required
def create_product():

    if request.method == 'POST' :
        name = request.form['name']
        description = request.form['description']
        items_count = request.form['items_count']
        type=1
        try:
            product = Products( name=name , description=description, items_count=items_count, type_id = type)
            db.session.add(product)
            db.session.commit()
        except:
            print("Something wrong")
        return redirect(url_for('products.index'))
    else:
        form = ProductForm()
        return render_template('products/create_product.html', form=form)


@products.route('/edit/<id>', methods=['POST','GET'])
@login_required
def edit_product(id):
    product = Products.query.filter(Products.id==id).first()

    if request.method == 'POST':
        form =ProductForm(formdata=request.form ,obj=product)
        form.populate_obj(product)
        db.session.commit()

        return redirect(url_for('products.index'))

    form = ProductForm(obj=product)
    return render_template('products/edit_product.html',product=product , form=form)


@products.route('/')
def index():
    products = Products.query.all()
    return render_template('products/index.html',products=products)

@products.route('/all')
def all_for_api():
    products = Products.query.all()
    result = []
    for product in products:
        result.append({
            'id': product.id,
            'title': product.name,
            'description': product.description,
            'count': product.items_count,
            'type': product.type.name
        })

    # return render_template('products/index.html',products=products)
    return jsonify(result)


@products.route('/<id>')
def product_detail(id):
    result = []
    product = Products.query.filter(Products.id == id).first()
    result.append({
        'id': product.id,
        'title': product.name,
        'description': product.description,
        'count': product.items_count
    })

    # return render_template('products/product_detail.html',product=product.type)
    return jsonify(result)