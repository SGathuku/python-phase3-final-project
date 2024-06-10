from app import create_app, db
from app.models import Category, Product

app = create_app()

def main_menu():
    print("Welcome to the Liquor Store CLI")
    while True:
        print("1. Manage Categories")
        print("2. Manage Products")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            manage_categories()
        elif choice == '2':
            manage_products()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_categories():
    while True:
        print("\nManage Categories")
        print("1. Create Category")
        print("2. Delete Category")
        print("3. Display All Categories")
        print("4. Find Category by Name")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_category()
        elif choice == '2':
            delete_category()
        elif choice == '3':
            display_all_categories()
        elif choice == '4':
            find_category_by_name()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def create_category():
    name = input("Enter category name: ")
    if Category.query.filter_by(name=name).first():
        print(f"Category '{name}' already exists.")
    else:
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        print(f"Category '{name}' created successfully.")

def delete_category():
    name = input("Enter category name to delete: ")
    category = Category.query.filter_by(name=name).first()
    if category:
        db.session.delete(category)
        db.session.commit()
        print(f"Category '{name}' deleted successfully.")
    else:
        print(f"Category '{name}' not found.")

def display_all_categories():
    categories = Category.query.all()
    for category in categories:
        print(category)

def find_category_by_name():
    name = input("Enter category name: ")
    category = Category.query.filter_by(name=name).first()
    if category:
        print(category)
    else:
        print(f"Category '{name}' not found.")

def manage_products():
    while True:
        print("\nManage Products")
        print("1. Create Product")
        print("2. Delete Product")
        print("3. Display All Products")
        print("4. Find Product by Name")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            display_all_products()
        elif choice == '4':
            find_product_by_name()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def create_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    category_name = input("Enter category name: ")
    category = Category.query.filter_by(name=category_name).first()
    if category:
        if Product.query.filter_by(name=name).first():
            print(f"Product '{name}' already exists.")
        else:
            new_product = Product(name=name, price=price, category=category)
            db.session.add(new_product)
            db.session.commit()
            print(f"Product '{name}' created successfully.")
    else:
        print(f"Category '{category_name}' not found.")

def delete_product():
    name = input("Enter product name to delete: ")
    product = Product.query.filter_by(name=name).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        print(f"Product '{name}' deleted successfully.")
    else:
        print(f"Product '{name}' not found.")

def display_all_products():
    products = Product.query.all()
    for product in products:
        print(product)

def find_product_by_name():
    name = input("Enter product name: ")
    product = Product.query.filter_by(name=name).first()
    if product:
        print(product)
    else:
        print(f"Product '{name}' not found.")

if __name__ == '__main__':
    with app.app_context():
        main_menu()
