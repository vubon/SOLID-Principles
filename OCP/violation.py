"""
Open Close Principle(OCP):
Software entities (classes, function, module) open for extension, but not for modification (or closed for modification)
Example:
Violation of OCP
"""


class Discount:
    """Demo customer discount class"""

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        """A discount method"""
        if self.customer == 'normal':
            return self.price * 0.2
        elif self.customer == 'vip':
            return self.price * 0.4


#
# This example is failed to pass the Open and Close Principle(OCP). Assume, we have a super VIP customer and we want to
# give a discount of 0.8 percentage. What would we do in this case? Maybe we will solve the problem this way
#

class Discounts:
    """Demo customer discounts class"""

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        """A discount method"""
        if self.customer == 'normal':
            return self.price * 0.2
        elif self.customer == 'vip':
            return self.price * 0.4
        elif self.customer == 'supvip':
            return self.price * 0.8

# But this solution violates the OCP. Because we can’t modify the give_discount method. Only we can extend the method.
