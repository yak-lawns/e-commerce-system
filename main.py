# main.py
from customer import Customer
from product import Product
from order import Order

# Create customers
customer1 = Customer(1, 'John Doe', 'john@example.com')
customer2 = Customer(2, 'Jane Smith', 'jane@example.com')

# Create products
product1 = Product(101, 'Laptop', 1200.0)
product2 = Product(102, 'Smartphone', 800.0)
product3 = Product(103, 'Headphones', 100.0)

# Create orders
order1 = Order(501, customer1, [product1, product2])
order2 = Order(502, customer2, [product2, product3])

# Display information
print(f"Customer: {customer1.get_name()}, Order Total: ${order1.calculate_total()}")
print(f"Customer: {customer2.get_name()}, Order Total: ${order2.calculate_total()}")
