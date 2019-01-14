from app import db

class Products(db.Model):
    __tablename__ = 'products'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(140))
    description=db.Column(db.Text)
    items_count=db.Column(db.Integer)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)


    def __init__(self,*args,**kwargs):
        super(Products,self).__init__(*args,**kwargs)


    def __repr__(self):
        return '<Products id: {}, name: {}>'.format(self.id,self.name)


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))

    product=db.relationship('Products',backref='type',lazy=True)


    def __init__(self,*args,**kwargs):
        super(Type,self).__init__(*args,**kwargs)

    def __repr__(self):
        return '<Type id: {}, name: {}>'.format(self.id,self.name)