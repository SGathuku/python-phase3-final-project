from flask import Flask, render_template, request, redirect, url_for
from models import session, Category, Product

app = Flask(__name__)

@app.route('/')
def index():
    categories = session.query(Category).all()
    products = session.query(Product).all()
    return render_template('index.html', categories=categories, products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category_name = request.form['category']
        category = session.query(Category).filter_by(name=category_name).first()
        if category:
            product = Product(name=name, price=price, category_id=category.id)
            session.add(product)
            session.commit()
            return redirect(url_for('index'))
        else:
            return "Category not found", 400
    categories = session.query(Category).all()
    return render_template('product_form.html', categories=categories)

@app.route('/delete_product/<int:id>')
def delete_product(id):
    product = session.query(Product).get(id)
    if product:
        session.delete(product)
        session.commit()
        return redirect(url_for('index'))
    else:
        return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)
