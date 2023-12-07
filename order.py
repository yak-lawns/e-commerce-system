# order.py
class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products

    def get_order_id(self):
        return self.order_id

    def get_customer(self):
        return self.customer

    def get_products(self):
        return self.products

    def calculate_total(self):
        return sum(product.get_price() for product in self.products)
