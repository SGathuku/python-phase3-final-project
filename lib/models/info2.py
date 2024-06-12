import sqlite3
from liquor_store import Category
from product import Product

from __init__ import conn, cursor

conn = sqlite3.connect('liquor_store.db')
cursor = conn.cursor()

additional_products = [
    ("Tusker", "Beer", 250.00),
    ("Tusker Lite", "Beer", 260.00),
    ("Tusker Cider", "Beer", 275.00),
    ("Budweiser", "Beer", 300.00),
    ("Jack Daniel's Old No.7", "Whiskey", 3864.71),
    ("Macallan 12 Year Double Cask", "Whiskey", 7730.72),
    ("Jameson Irish Whiskey", "Whiskey", 4128.00),
    ("Bulleit Bourbon", "Whiskey", 4129.54),
    ("Absolut Vodka", "Vodka", 2580.72),
    ("Grey Goose", "Vodka", 3871.88),
    ("Belvedere Vodka", "Vodka", 4517.49),
    ("Ketel One", "Vodka", 3226.42)
]

for product_name, category_name, product_price in additional_products:
    category = Category.create(category_name)
    Product.create(product_name, product_price, category.id)

conn.commit()
conn.close()
