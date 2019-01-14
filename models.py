from app import db

class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(140))
    description=db.Column(db.Text)
    items_count=db.Column(db.Integer)

    def __init__(self,*args,**kwargs):
        super(Products,self).__init__(*args,**kwargs)

    def __repr__(self):
        return '<Products id: {}, name: {}>'.format(self.id,self.name)