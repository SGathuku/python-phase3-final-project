from helpers import (
    exit_program,
    list_categories,
    add_category,
    list_products,
    add_product
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2":
            name = input("Enter the category name: ")
            add_category(name)
        elif choice == "3":
            list_products()
        elif choice == "4":
            name = input("Enter the product name: ")
            price = input("Enter the product price: ")
            category_name = input("Enter the category name: ")
            add_product(name, price, category_name)
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List categories")
    print("2. Add a category")
    print("3. List products")
    print("4. Add a product")

if __name__ == "__main__":
    main()
