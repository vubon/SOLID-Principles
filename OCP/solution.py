# Solution

class Discounts:
    """Demo customer discounts class"""

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        """A discount method"""
        return self.price * 0.2


class VIPDiscount(Discounts):
    """Demo VIP customer discount class"""

    def get_discount(self):
        """A discount method"""
        return super().get_discount() * 2


class SuperVIPDiscount(VIPDiscount):
    """Demo super vip customer discount class"""

    def get_discount(self):
        """A discount method"""
        return super().get_discount() * 2
