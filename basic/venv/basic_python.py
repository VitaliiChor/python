shop= "Over 20 Years of Experience To Give You Great Deals on Quality Home Products and More. Shop MacBooks You Love at Overstock, with Free Shipping on Everything* and Easy Returns."

macBookPro15 = "Configure to Order. Configure your MacBook Pro with these options, only at apple.com: 2.4GHz 8-core Intel Core i9, Turbo Boost"
macBookPro15_price = 1000

macBookPro13 = "Configure to Order. Configure your MacBook Pro with these options, only at apple.com: 2.1GHz 4-core Intel Core i5, Turbo Boost"
macBookPro13_price = 800

total_price = 0

total_price += macBookPro15_price
total_price += macBookPro13_price

sale_rate = (total_price / 5) + total_price

customer_total = "Customer One Total: "
customer_description = "Customer One Description: "
customer_description = macBookPro15 + macBookPro13

print(customer_description)
print(customer_total, sale_rate)







