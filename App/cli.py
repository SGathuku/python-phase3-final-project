import sys
from models import Liquor, db
from config import Config
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def display_menu():
    print("1. Add Liquor")
    print("2. Delete Liquor")
    print("3. View All Liquors")
    print("4. Find Liquor by Name")
    print("5. Exit")

def add_liquor():
    name = input("Enter liquor name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    Liquor.create(name, category, price, stock)
    print("Liquor added successfully!")

def delete_liquor():
    name = input("Enter liquor name to delete: ")
    Liquor.delete_by_name(name)
    print("Liquor deleted successfully!")

def view_all_liquors():
    liquors = Liquor.get_all()
    for liquor in liquors:
        print(f"Name: {liquor.name}, Category: {liquor.category}, Price: {liquor.price}, Stock: {liquor.stock}")

def find_liquor():
    name = input("Enter liquor name to find: ")
    liquor = Liquor.find_by_name(name)
    if liquor:
        print(f"Name: {liquor.name}, Category: {liquor.category}, Price: {liquor.price}, Stock: {liquor.stock}")
    else:
        print("Liquor not found")

def main():
    with app.app_context():
        while True:
            display_menu()
            choice = input("Enter choice: ")
            if choice == '1':
                add_liquor()
            elif choice == '2':
                delete_liquor()
            elif choice == '3':
                view_all_liquors()
            elif choice == '4':
                find_liquor()
            elif choice == '5':
                sys.exit()
            else:
                print("Invalid choice, please try again")

if __name__ == '__main__':
    main()
