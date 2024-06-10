from App.db import db

class Liquor(db.Model):
    __tablename__ = 'liquors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    @property
    def stock_value(self):
        return self.price * self.stock

    @staticmethod
    def create(name, category, price, stock):
        liquor = Liquor(name, category, price, stock)
        db.session.add(liquor)
        db.session.commit()

    @staticmethod
    def delete_by_name(name):
        liquor = Liquor.query.filter_by(name=name).first()
        if liquor:
            db.session.delete(liquor)
            db.session.commit()

    @staticmethod
    def get_all():
        return Liquor.query.all()

    @staticmethod
    def find_by_name(name):
        return Liquor.query.filter_by(name=name).first()
