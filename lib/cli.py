from .liquor_store import Category, Product
from .helpers import exit_program, enter_name, enter_price, enter_category

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
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Enter name of liquor: ")
    print("2. Enter price of liquor: ")
    print("3. Enter category of liquor:")

if __name__ == "__main__":
    main()
