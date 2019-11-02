"""
Example:
Violation of LSP

How does it violate the LSP?
In Bicycle class violates the LSP. Cause in the Vehicle class has engine method.
But by naturally a bicycle has no engine. So we could not start any engine.
"""


class Vehicle:
    """A demo Vehicle class"""

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        """Get vehicle name"""
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        """Get vehicle speed"""
        return f"The vehicle speed {self.speed}"

    def engine(self):
        """A vehicle engine"""
        pass

    def start_engine(self):
        """A vehicle engine start"""
        self.engine()


class Car(Vehicle):
    """A demo Car Vehicle class"""

    def start_engine(self):
        pass


class Bicycle(Vehicle):
    """A demo Bicycle Vehicle class"""

    def start_engine(self):
        pass
