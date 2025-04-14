#The Description of the product 1
lovely_loveseat_description = """
Lovely Loveseat. Tufted Polyster blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.

"""
#Price
lovely_loveseat_price = 254.000

#The Description of The product 2
stylish_settee_description ="""
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.

"""
#Price
stylish_settee_price = 180.50

# The Description of The Product 3
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.

"""
# Price
luxurious_lamp_price = 52.15

#Tax
sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""

#Purchase the product 1
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

#Purchase the product 2
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
customer_one_itemization += luxurious_lamp_description

#Purchase the product 3
customer_one_total += stylish_settee_price
customer_one_tax = customer_one_total * sales_tax
customer_total = customer_one_total - customer_one_tax
print("Customer One Items:", customer_one_itemization)
print("Customer One Total:", customer_total)

