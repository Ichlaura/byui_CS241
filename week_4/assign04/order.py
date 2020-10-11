"""
File: order.py
Author: Lewis Lockhart
"""


class Order:
    """
    The Order class has an id and products list.
    It can:
        get_subtotal()
        get_tax()
        get_total()
        add_product()
        display_receipt()
    """
    def __init__(self):
        """ Initializes values id and products. """
        self.id = ""
        self.products = []

    def get_subtotal(self):
        """ Sums the price of each product and returns it. """
        s_total = 0.0
        for i in self.products:
            s_total += i.get_total_price()
        return s_total

    def get_tax(self):
        """ Returns 6.5% times the subtotal. """
        tax = self.get_subtotal() * 0.065
        return tax

    def get_total(self):
        """ Returns the subtotal plus the tax. """
        sub_total = self.get_subtotal()
        t_tax = self.get_tax()
        return sub_total + t_tax

    def add_product(self, _product):
        """ Adds the provided product to the list. """
        self.products.append(_product)

    def display_receipt(self):
        """ Displays a receipt. """
        print(f"Order: {self.id}")
        for i in self.products:
            i.display()
        print(f"Subtotal: ${format(self.get_subtotal(), '.2f')}")
        print(f"Tax: ${format(self.get_tax(), '.2f')}")
        print(f"Total: ${format(self.get_total(), '.2f')}")
