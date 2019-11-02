"""
Solution:
"""


class Shape:
    """A demo shape class"""

    def draw(self):
        """Draw a shape"""
        raise NotImplemented


class Circle(Shape):
    """A demo circle class"""

    def draw(self):
        """Draw a circle"""
        pass


class Square(Shape):
    """A demo square class"""

    def draw(self):
        """Draw a square"""
        pass


# Another example
class BankAccount:
    """A demo Bank Account class"""

    def __init__(self, balance: float, account: str):
        self.account = {f"{account}": balance}

    def balance(self, account: str):
        """Get current balance"""
        raise NotImplemented


class Deposit(BankAccount):
    """A demo circle class"""

    def balance(self, account: str):
        """Get current balance"""
        return self.account.get(account)

    def deposit(self, amount: float, account: str):
        """Deposit a new amount"""
        current = self.balance(account)
        new_amount = current + amount
        self.account.update({account: new_amount})
