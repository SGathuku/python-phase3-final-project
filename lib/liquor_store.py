# liquor_store.py
from lib import conn, cursor

class Category:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"<Category(name={self.name}, id={self.id})>"

    @classmethod
    def create_table(cls):
        cursor.execute('''CREATE TABLE IF NOT EXISTS category (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL
                        )''')
        conn.commit()

    def save(self):
        sql = '''
            INSERT INTO category (name) VALUES (?);
        '''
        cursor.execute(sql, (self.name,))
        conn.commit()
        
        self.id = cursor.lastrowid
        
    @classmethod
    def create(cls, name):
        category = cls(name)
        category.save()
        
        return category

    @classmethod
    def get_all(cls):
        cursor.execute("SELECT * FROM category")
        rows = cursor.fetchall()
        categories = []
        for row in rows:
            category = Category(row[1], row[0])
            categories.append(category)
        return categories

    @classmethod
    def display_all(cls):
        cursor.execute("SELECT * FROM category")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}")

    @classmethod
    def delete_by_id(cls, id):
        sql = "DELETE FROM category WHERE id = ?"
        cursor.execute(sql, (id,))
        conn.commit()

class Product:
    def __init__(self, name, price, category_id, id=None):
        self.name = name
        self.price = price
        self.category_id = category_id
        self.id = id

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, category_id={self.category_id})>"

    @classmethod
    def create_table(cls):
        cursor.execute("DROP TABLE IF EXISTS product")
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS product (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price REAL NOT NULL,
                            category_id INTEGER,
                            FOREIGN KEY (category_id) REFERENCES category(id)
                        )''')
        conn.commit()

    def save(self):
        sql = '''
            INSERT INTO product (name, price, category_id) VALUES (?, ?, ?);
        '''
        cursor.execute(sql, (self.name, self.price, self.category_id))
        conn.commit()
        
        self.id = cursor.lastrowid
        
    @classmethod
    def create(cls, name, price, category_id):
        product = cls(name, price, category_id)
        product.save()
        
        return product

    @classmethod
    def get_all(cls):
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            product = Product(row[1], row[2], row[3], row[0])
            products.append(product)
        return products

    @classmethod
    def get_by_name(cls, name):
        sql = "SELECT * FROM product WHERE name = ?"
        cursor.execute(sql, (name,))
        row = cursor.fetchone()
        if row:
            return Product(row[1], row[2], row[3], row[0])
        else:
            return None

    @classmethod
    def get_by_id(cls, id):
        sql = "SELECT * FROM product WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        if row:
            return Product(row[1], row[2], row[3], row[0])
        else:
            return None

    @classmethod
    def delete_by_id(cls, id):
        sql = "DELETE FROM product WHERE id = ?"
        cursor.execute(sql, (id,))
        conn.commit()

def initialize_db():
    Category.create_table()
    Product.create_table()

    # Sample data initialization
    liquor_tables = [
        ("Beer", "Tusker", 2.5),
        ("Beer", "Tusker Lite", 2.7),
        ("Beer", "Tusker Cider", 3.0),
        ("Beer", "Budweiser", 3.5),
        ("Whiskey", "Jack Daniel's Old No.7", 30.0),
        ("Whiskey", "Macallan 12 Year Double Cask", 65.0),
        ("Whiskey", "Jameson Irish Whiskey", 25.0),
        ("Whiskey", "Bulleit Bourbon", 40.0),
        ("Vodka", "Absolut Vodka", 20.0),
        ("Vodka", "Grey Goose", 50.0),
        ("Vodka", "Belvedere Vodka", 45.0),
        ("Vodka", "Ketel One", 30.0)
    ]

    for category_name, product_name, product_price in liquor_tables:
        category = Category.create(category_name)
        Product.create(product_name, product_price, category.id)

if __name__ == "__main__":
    initialize_db()
