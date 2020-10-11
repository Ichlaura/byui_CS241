"""
File: product.py
Author: Lewis Lockhart
"""


class Product:
    """
    The Product class has id, name, price, quantity.
    It can:
        get_total_price()
        display()
    """
    def __init__(self, id, name, price, quantity):
        """ Initializes to the values that were passed. """
        self.id = id
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def get_total_price(self):
        """ Returns the price multiplied by the quantity. """
        return self.price * self.quantity

    def display(self):
        """ Displays the products name, quantity, and total price. """
        print(f"{self.name} ({self.quantity}) - ${format(self.get_total_price(), '.2f')}")
