from liquor_store import Product

# CREATING PRODUCT TABLE

Product.create_table()

Product_table1 = Product.create(
    name = "Tusker", category= "Beer", price= 250.00
)

Product_table2 = Product.create(
    name = "Tusker Lite", category= "Beer", price= 260.00
)

Product_table3 = Product.create(
    name = "Tusker Cider", category= "Beer", price= 275.00
)

Product_table4 = Product.create(
    name = "Budweiser", category= "Beer", price= 300.00
)

Product_table5 = Product.create(
    name = "Jack Daniel's OLd No.7", category= "Whiskey", price= 3864.71
)

Product_table6 = Product.create(
    name = "Macallan 12 Year Double Cask", category= "Whiskey", price= 7730.72
)

Product_table7 = Product.create(
    name = "Jameson Irish Whiskey", category= "Whiskey", price= 4128.00  
)

Product_table8 = Product.create(
    name = "Bulleit Bourbon", category= "Whiskey", price= 4129.54
)

Product_table9 = Product.create(
    name = "Absolut Vodka", category= "Vodka", price= 2580.72
)

Product_table10 = Product.create(
    name = "Grey Goose", category= "Vodka", price= 3871.88  
)

Product_table11 = Product.create(
    name = "Belvedere Vodka", category= "Vodka", price= 4517.49
)

Product_table12 = Product.create(
    name = "Ketel One", category= "Vodka", price= 3226.42
)