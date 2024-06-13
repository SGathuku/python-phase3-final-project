from lib import conn, cursor

class Product:
    def __init__(self, name, price, category_id):
        self.name = name
        self.price = price
        self.category_id = category_id

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, category_id={self.category_id})>"

    @classmethod
    def create_table(cls):
        cursor.execute('''CREATE TABLE IF NOT EXISTS product (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price REAL NOT NULL,
                            category_id INTEGER,
                            FOREIGN KEY (category_id) REFERENCES category(id)
                        )''')
        conn.commit()

    def save(self, name, price, category_id):
        self.name = name
        self.price = price
        self.category_id = category_id

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
