# display.py
from lib.liquor_store import Category, Product

def display_data():
    print("Categories:")
    categories = Category.get_all()
    for category in categories:
        print(f"ID: {category.id}, Name: {category.name}")

    print("\nProducts:")
    products = Product.get_all()
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category ID: {product.category_id}")

if __name__ == "__main__":
    display_data()
