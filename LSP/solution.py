"""
Refactor the code and make a solution for this problem.
Solution:
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


class VehicleWithoutEngine(Vehicle):
    """A demo Vehicle without engine class"""

    def start_moving(self):
        """Moving"""
        raise NotImplemented


class VehicleWithEngine(Vehicle):
    """A demo Vehicle engine class"""

    def engine(self):
        """A vehicle engine"""
        pass

    def start_engine(self):
        """A vehicle engine start"""
        self.engine()


class Car(VehicleWithEngine):
    """A demo Car Vehicle class"""

    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):
    """A demo Bicycle Vehicle class"""

    def start_moving(self):
        pass
