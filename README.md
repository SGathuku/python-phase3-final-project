# LIQUOR STORE MANAGEMENT SYSTEM

This is a simple command-line application for managing a liquor store inventory. It allows the user to enter the name, price, and category of different liquors and stores this information in an SQLite database.

By  **Gathuku Samwel**

## Project Description

* The Liquor Store Management System is a command-line application designed to help manage the inventory of a liquor store.
* This simple and user-friendly tool allows users to enter and delete details about liquors, including their names, prices, and categories, and stores this information in an SQLite database for persistent storage.
* The system provides a menu-driven interface where users can easily add new liquor entries and update existing ones. This project is ideal for small liquor store owners or managers who need an efficient way to keep track of their stock.

### Requirements

-Python 3.x
-SQLite3

### Installation process

1. Clone the Repository:

```bash
git clone https://github.com/SGathuku/python-phase3-final-project.git
```

or by downloading a ZIP file of the code.

2.Install any required Python packages (if any):

``` python
pipenv install
```

3.Run the CLI:

```sh
python -m lib/cli.py
```

## Features

1.Initialize Database: Create tables for categories and products, and populate them with sample data.

2.Add Liquor Details:

*Add Liquor Name: Allows the user to enter and store the name of a liquor.

*Add Liquor Price: Allows the user to enter and store the price of a liquor.

*Add Liquor Category: Allows the user to enter and store the category of a liquor.

3.Persistent Storage: Stores all entered data persistently in an SQLite database.

4.Menu-Driven Interface: Provides a simple and intuitive menu-driven interface for users to interact with the system.

5.Data Validation: Ensures that the input data (such as price) is of the correct type.

6.Update Existing Entries: Allows users to update the price and category of the most recently entered liquor.

7.Search Product:

*Search Product by ID: Search for a product in the database by its ID.

*Search Product by Name: Search for a product in the database by its name.

8.Delete Product:

*Delete Product by ID: Delete a product from the database using its ID.

*Delete Product by Name: Delete a product from the database using its name.

9.Exit Program: Allows users to exit the program gracefully, ensuring that all data is saved and the database connection is closed properly.

## Technologies Used

-**Python 3.x**: The main programming language used to develop the application. Python is known for its simplicity and readability, making it a great choice for a command-line application.
-**SQLite3**: A lightweight, disk-based database that doesn’t require a separate server process. SQLite is integrated into the Python standard library, making it easy to use for database operations within a Python application.
-**sqlite3 Python Module**: This module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249. It allows the application to connect to an SQLite database, execute SQL queries, and manage data.
-**SQL**: The standard language for relational database management and manipulation. SQL is used within the application to create the database schema and perform CRUD (Create, Read, Update, Delete) operations.

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
SOFTWARE
