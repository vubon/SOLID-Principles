"""
Single Responsibility Principle(SRP):
A class should have only one responsibility and only one reason to change. That means a class does not perform multiple
jobs.

Example:
Violation of SRP

How does it violate the SRP?
In the account class, I am performing two tasks. One is stored data and another one gets account number. So it violates
the SRP.
"""


class Account:
    """Demo bank account class """

    def __init__(self, account_no: str):
        self.account_no = account_no

    def get_account_number(self):
        """Get account number"""
        return self.account_no

    def save(self):
        """Save account number into DB"""
        pass


