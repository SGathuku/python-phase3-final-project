from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

engine = create_engine('mysql+mysqlconnector://samwel:1996bandana_254@127.0.0.1:3306/liquor_store')

Session = sessionmaker(bind=engine)
session = Session()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    products = relationship('Product', back_populates='category')

    def __repr__(self):
        return f"<Category(name={self.name})>"

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category', back_populates='products')

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"

Base.metadata.create_all(engine)

def menu():
    while True:
        print("\nMenu:")
        print("1. Add Category")
        print("2. Add Product")
        print("3. Delete Category")
        print("4. Delete Product")
        print("5. View All Categories")
        print("6. View All Products")
        print("7. Find Category by Name")
        print("8. Find Product by Name")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_category()
        elif choice == '2':
            add_product()
        elif choice == '3':
            delete_category()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            view_all_categories()
        elif choice == '6':
            view_all_products()
        elif choice == '7':
            find_category_by_name()
        elif choice == '8':
            find_product_by_name()
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")

def add_category():
    name = input("Enter category name: ")
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' added.")

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    category_name = input("Enter category name: ")
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        product = Product(name=name, price=price, category_id=category.id)
        session.add(product)
        session.commit()
        print(f"Product '{name}' added.")
    else:
        print(f"Category '{category_name}' not found.")

def delete_category():
    name = input("Enter category name to delete: ")
    category = session.query(Category).filter_by(name=name).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category '{name}' deleted.")
    else:
        print(f"Category '{name}' not found.")

def delete_product():
    name = input("Enter product name to delete: ")
    product = session.query(Product).filter_by(name=name).first()
    if product:
        session.delete(product)
        session.commit()
        print(f"Product '{name}' deleted.")
    else:
        print(f"Product '{name}' not found.")

def view_all_categories():
    categories = session.query(Category).all()
    for category in categories:
        print(category)

def view_all_products():
    products = session.query(Product).all()
    for product in products:
        print(product)

def find_category_by_name():
    name = input("Enter category name: ")
    category = session.query(Category).filter_by(name=name).first()
    if category:
        print(category)
    else:
        print(f"Category '{name}' not found.")

def find_product_by_name():
    name = input("Enter product name: ")
    product = session.query(Product).filter_by(name=name).first()
    if product:
        print(product)
    else:
        print(f"Product '{name}' not found.")

if __name__ == '__main__':
    menu()
