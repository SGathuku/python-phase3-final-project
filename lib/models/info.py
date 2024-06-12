from liquor_store import Category

Category.create_table()

liquor_table1 = Category.create(
   name= "Beer" 
)

liqour_table2 = Category.create(
    name="Beer" 
)

liqour_table3 = Category.create(
    name="Beer" 
)

liqour_table4 = Category.create(
    name="Beer" 
)
liqour_table5 = Category.create(
    name="Whiskey" )

liqour_table6 = Category.create(
    name="Whiskey" 
)

liqour_table7 = Category.create(
    name="Whiskey" 
)

liqour_table8 = Category.create(
    name="Whiskey"
)

liqour_table9 = Category.create(
    name="Vodka" , Product = "Absolut Vodka"
)

liqour_table10 = Category.create(
    name="Vodka" , Product = "Grey Goose"
)

liqour_table11 = Category.create(
    name="Vodka" , Product = "Belvedere Vodka"
)

liqour_table12 = Category.create(
    name="Vodka" , Product = "Ketel One"
)

