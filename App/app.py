from flask import Flask, render_template
from config import Config
from db import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_liquor')
def add_liquor():
    return render_template('add_liquor.html')

@app.route('/delete_liquor')
def delete_liquor():
    return render_template('delete_liquor.html')

@app.route('/view_liquors')
def view_liquors():
    return render_template('view_liquors.html')

if __name__ == '__main__':
    app.run(debug=True)
