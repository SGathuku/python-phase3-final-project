# cli.py
from .liquor_store import Category, Product
from .helpers import exit_program

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            enter_name()
        elif choice == "2":
            enter_price()
        elif choice == "3":
            enter_category()
        elif choice == "4":
            search_by_id()
        elif choice == "5":
            search_by_name()
        elif choice == "6":
            delete_by_id()
        elif choice == "7":
            delete_by_name()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Enter name of liquor")
    print("2. Enter price of liquor")
    print("3. Enter category of liquor")
    print("4. Search liquor by ID")
    print("5. Search liquor by name")
    print("6. Delete liquor by ID")
    print("7. Delete liquor by name")

def enter_name():
    name = input("Enter the name of the liquor: ")
    category_id = select_category()
    if category_id:
        product = Product.create(name, 0.0, category_id)
        print(f"Product '{product.name}' created with ID {product.id}")

def enter_price():
    try:
        price = float(input("Enter the price of the liquor: "))
        product_id = input("Enter the ID of the product to update: ")
        product = Product.get_by_id(product_id)
        if product:
            product.price = price
            product.save()
            print(f"Price updated for product: {product}")
        else:
            print(f"No product found with ID {product_id}")
    except ValueError:
        print("Invalid price format. Please enter a valid number.")

def enter_category():
    category = input("Enter the category of the liquor: ")
    category = Category.create(category)
    print(f"Category '{category.name}' created with ID {category.id}")

def search_by_id():
    product_id = input("Enter the ID of the product to search: ")
    product = Product.get_by_id(product_id)
    if product:
        print(f"Found product: {product}")
    else:
        print(f"No product found with ID {product_id}")

def search_by_name():
    product_name = input("Enter the name of the product to search: ")
    product = Product.get_by_name(product_name)
    if product:
        print(f"Found product: {product}")
    else:
        print(f"No product found with name '{product_name}'")

def delete_by_id():
    product_id = input("Enter the ID of the product to delete: ")
    product = Product.get_by_id(product_id)
    if product:
        Product.delete_by_id(product_id)
        print(f"Product with ID {product_id} has been deleted.")
    else:
        print(f"No product found with ID {product_id}")

def delete_by_name():
    product_name = input("Enter the name of the product to delete: ")
    product = Product.get_by_name(product_name)
    if product:
        Product.delete_by_id(product.id)
        print(f"Product with name '{product_name}' has been deleted.")
    else:
        print(f"No product found with name '{product_name}'")

def select_category():
    Category.display_all()
    category_id = input("Enter the ID of the category: ")
    return category_id

if __name__ == "__main__":
    main()
