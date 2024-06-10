# FEEL THE VIBE ONLINE LIQUOR STORE

A simple PYTHON APPLICATION THAT ONE CAN PURCHASE LIQUOR FROM THE INTERNET THAT INCORPORATES HTML, CSS AND JAVASCRIPT LANGUAGES.

By  **Gathuku Samwel**

## Project Description

"FEEL THE VIBE" Online Liquor Store is a dynamic web application for managing and purchasing liquor products.

Built with Flask, SQLAlchemy, and MySQL, this project demonstrates an implementation of an e-commerce platform.

Users can view categories and products, with a command-line interface (CLI) for administrative tasks such as creating and managing product categories and individual products.

### Requirements

* A computer with a bash terminal and all necessary dependencies and application installed.

* Python: Ensure you have Python 3.8 or higher installed. You can download it from python.org.

* MySQL: Install MySQL server and client. You can download MySQL from mysql.com.

* Pipenv: Install Pipenv for managing the virtual environment and dependencies. You can install Pipenv using pip: "pip install pipenv" on your terminal or editor.

### Installation process

1. Clone the Repository:

```bash
git clone https://github.com/SGathuku/python-phase3-final-project.git
```

or by downloading a ZIP file of the code.

2. Create and Activate Virtual Environment:

```sh
pipenv install
pipenv shell
```

3. Configure the Database:

* Create a MySQL database:

```sh

mysql -u root -p
CREATE DATABASE liquor_store;
```

* Update config.py with your MySQL database credentials:

``` python
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/liquor_store'
```

4. Initialize the Database:

```sh

flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

5. Run the Web Application:

```sh
flask run
```

* Access the application at http://127.0.0.1:5000.

6. Run the CLI:

```sh
python app/cli.py
```

## Features

1) Dynamic Web Interface: User-friendly interface with sliding and stylish background images, ensuring a visually appealing and responsive design.

2) Product and Category Management: View categories and products with the ability to filter by category.

3) CLI for Administrative Tasks:

* Create, delete, and view categories and products.
* Find products and categories by name.
* ORM and Database: Utilizes SQLAlchemy for object-relational mapping with a MySQL database backend.
* Responsive Design: Uses HTML, CSS, and JavaScript to provide a seamless user experience.

## Technologies Used

Frontend:

1) HTML
2) CSS
3) JavaScript

Backend:

1) Python
2) SQLAlchemy
3) MySQL

CLI:

1) Python

## Support and Contact details

Incase of any query, need for collaboration or issues with this code, feel free to reach me at
<samwel.gathuku@student.moringaschool.com>

## License

MIT License

Copyright (c) 2024 SGathuku

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

