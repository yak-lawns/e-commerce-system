# customer.py
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email
