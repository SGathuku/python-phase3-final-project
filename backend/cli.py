import click
from backend.models import Category, Product
from backend.database import init_db

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    init_db()
    click.echo('Initialized the database.')

@cli.group()
def category():
    pass

@category.command()
@click.argument('name')
def create(name):
    Category.create(name)
    click.echo(f'Category {name} created.')

@category.command()
@click.argument('name')
def delete(name):
    Category.delete(name)
    click.echo(f'Category {name} deleted.')

@category.command()
def list():
    categories = Category.get_all()
    for category in categories:
        click.echo(category.name)

@category.command()
@click.argument('name')
def find(name):
    category = Category.find_by_name(name)
    if category:
        click.echo(f'Category found: {category.name}')
    else:
        click.echo('Category not found.')

@cli.group()
def product():
    pass

@product.command()
@click.argument('name')
@click.argument('price', type=float)
@click.argument('category_name')
def create(name, price, category_name):
    category = Category.find_by_name(category_name)
    if category:
        Product.create(name, price, category.id)
        click.echo(f'Product {name} created under category {category_name}.')
    else:
        click.echo('Category not found.')

@product.command()
@click.argument('name')
def delete(name):
    Product.delete(name)
    click.echo(f'Product {name} deleted.')

@product.command()
def list():
    products = Product.get_all()
    for product in products:
        click.echo(f'{product.name} - ${product.price}')

@product.command()
@click.argument('name')
def find(name):
    product = Product.find_by_name(name)
    if product:
        click.echo(f'Product found: {product.name} - ${product.price}')
    else:
        click.echo('Product not found.')

if __name__ == '__main__':
    cli()
