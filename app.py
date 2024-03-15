from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Connection string for Azure SQL Database
conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=azureassignment.database.windows.net;DATABASE=azureassignment;UID=azureassignment;PWD=Harmeet12@;Encrypt=yes;TrustServerCertificate=no'

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_price = request.form['product_price']
        product_description = request.form['product_description']
        product_image = request.form['product_image']
        product_category = request.form['product_category']

        # Add more fields as needed
        try:
            with pyodbc.connect(conn_str) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("INSERT INTO Products (ProductName, Price, Description, ImageURL, Category) VALUES (?, ?, ?, ?, ?)", (product_name, product_price, product_description, product_image, product_category))
                    conn.commit()
            return render_template('add_product_success.html')
            #return "Product added successfully!"
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('add_product.html')

@app.route('/list_products')
def list_products():
    try:
        with pyodbc.connect(conn_str) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Products")
                products = cursor.fetchall()
        return render_template('list_products.html', products=products)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    try:
        with pyodbc.connect(conn_str) as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Products WHERE ProductID = ?", (product_id,))
                conn.commit()
        return redirect(url_for('list_products'))
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)