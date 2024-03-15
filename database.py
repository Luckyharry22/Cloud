import pyodbc

class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            self.cursor = self.conn.cursor()
            print("Connected to the database")
        except Exception as e:
            print("Error connecting to the database:", e)

    def create_products_table(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Products (ProductName VARCHAR(255) NOT NULL)")
            self.conn.commit()
            print("Products table created successfully")
        except Exception as e:
            print("Error creating Products table:", e)

    def add_product(self, name):
        try:
            self.cursor.execute("INSERT INTO Products (ProductName) VALUES (?)", (name,))
            self.conn.commit()
            print("Product added successfully")
        except Exception as e:
            print("Error adding product:", e)

    def list_products(self):
        try:
            self.cursor.execute("SELECT * FROM Products")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print("Error listing products:", e)
