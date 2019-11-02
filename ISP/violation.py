"""
Example:
Violation of ISP

How does it violate the ISP?
In the above example, we need to call an unnecessary method in the Circle class.
Hence the example violated the Interface Segregation Principle.
"""


class Shape:
    """A demo shape class"""

    def draw_circle(self):
        """Draw a circle"""
        raise NotImplemented

    def draw_square(self):
        """ Draw a square"""
        raise NotImplemented


class Circle(Shape):
    """A demo circle class"""


def draw_circle(self):
    """Draw a circle"""
    pass


def draw_square(self):
    """ Draw a square"""
    pass
