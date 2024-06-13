from .liquor_store import Category, Product

def exit_program():
    print("Goodbye!")
    exit()

def enter_name():
    name_liquor = input("Enter name of liquor: ")
    print(f"Liquor name entered: {name_liquor}")
    category_name = input("Enter category of liquor: ")
    category = Category.create(name=category_name)
    price = input("Enter price of liquor: ")
    product = Product.create(name=name_liquor, price=float(price), category_id=category.id)
    print(f"Product added: {product}")

def enter_price():
    price_liquor = input("Enter price of liquor: ")
    print(f"Liquor price entered: {price_liquor}")

def enter_category():
    category_name = input("Enter category of liquor: ")
    category = Category.create(name=category_name)
    print(f"Category added: {category}")
