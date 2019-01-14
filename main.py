from API.app import app
from API.app import db

from products.blueprint import products

import viev

app.register_blueprint(products, url_prefix='/products')

if __name__=='__main__':
    app.run()