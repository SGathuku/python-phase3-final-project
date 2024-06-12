from models import session, Category, Product

def list_categories():
    categories = session.query(Category).all()
    for category in categories:
        print(f"ID: {category.id}, Name: {category.name}")

def add_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Added category: {name}")

def list_products():
    products = session.query(Product).all()
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category.name}")

def add_product(name, price, category_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        product = Product(name=name, price=price, category_id=category.id)
        session.add(product)
        session.commit()
        print(f"Added product: {name}")
    else:
        print(f"Category {category_name} not found")

def exit_program():
    print("Goodbye!")
    exit()
