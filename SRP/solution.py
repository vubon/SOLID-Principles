"""
Solution: A common solution to this problem is to apply the facade pattern. Let’s create another class and this class
will handle database management job and the account class will only handle his properties.
"""


class AccountDB:
    """Account DB management class """

    def get_account_number(self, _id):
        """Get account number"""
        pass

    def account_save(self, obj):
        """Save account number into DB"""
        pass


class Account:
    """Demo bank account class """

    def __init__(self, account_no: str):
        self.account_no = account_no
        self._db = AccountDB()

    def get_account_number(self):
        """Get account number"""
        return self.account_no

    def get(self, _id):
        """
        :param _id:
        :return:
        """
        return self._db.get_account_number(_id=_id)

    def save(self):
        """account save"""
        self._db.account_save(obj=self)
