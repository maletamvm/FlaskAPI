from app import app
from app import db

from products.blueprint import products

import viev

app.register_blueprint(products, url_prefix='/product')

if __name__=='__main__':
    app.run()