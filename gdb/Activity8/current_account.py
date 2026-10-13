from gdb.Activity1.account import Account
from gdb.Activity5.account import InvalidAmountException, InsufficientBalanceException, InactiveAccountException


class CurrentAccount(Account):
    def __init__(self, account_number, name, age, balance, overdraft_limit=20000.0, status="Active"):
        super().__init__(account_number, name, age, balance, account_type="Current", status=status)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")

        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")

        if amount > self._balance + self._overdraft_limit:
            raise InsufficientBalanceException(f"Insufficient balance. Available including overdraft: {self._balance + self._overdraft_limit}, Requested: {amount}")

        self._balance -= amount