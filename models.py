from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://username:password@localhost/liquor_store')
Session = sessionmaker(bind=engine)
session = Session()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Category(name={self.name})>"

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category")

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"

Base.metadata.create_all(engine)
