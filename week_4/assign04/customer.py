"""
File: customer.py
Author: Lewis Lockhart
"""


class Customer:
    """
    The Product class has id, name, and orders list.
    It can:
        get_order_count()
        get_total()
        add_order()
        display_summary()
        display_receipts()
    """
    def __init__(self):
        """ Initializes values id, name and orders. """
        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        """ Returns the number of orders. """
        count = len(self.orders)
        return count

    def get_total(self):
        """ Returns the total price of all orders combined. """
        t_total = 0.0
        for i in self.orders:
            t_total += i.get_total()
        return t_total

    def add_order(self, _order):
        """ Adds the provided order to the list of orders. """
        self.orders.append(_order)

    def display_summary(self):
        """ Displays a summary. """
        print(f"Summary for customer '{self.id}':\nName: {self.name}")
        print(f"Orders: {self.get_order_count()}")
        print(f"Total: ${format(self.get_total(), '.2f')}")

    def display_receipts(self):
        """ Displays all the orders' receipts. """
        print(f"Detailed receipts for customer '{self.id}':\nName: {self.name}")
        for i in self.orders:
            print("")
            i.display_receipt()

