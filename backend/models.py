from backend.database import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        category = cls(name=name)
        db.session.add(category)
        db.session.commit()
        return category

    @classmethod
    def delete(cls, name):
        category = cls.find_by_name(name)
        if category:
            db.session.delete(category)
            db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))

    def __init__(self, name, price, category_id):
        self.name = name
        self.price = price
        self.category_id = category_id

    @classmethod
    def create(cls, name, price, category_id):
        product = cls(name=name, price=price, category_id=category_id)
        db.session.add(product)
        db.session.commit()
        return product

    @classmethod
    def delete(cls, name):
        product = cls.find_by_name(name)
        if product:
            db.session.delete(product)
            db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
