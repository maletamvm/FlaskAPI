from wtforms import Form, StringField ,TextAreaField


class ProductForm(Form):
    name =StringField('Name'),
    description = TextAreaField('description')
    items_count= StringField('items_count')