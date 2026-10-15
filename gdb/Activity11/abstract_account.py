from gdb.Activity11.iaccount import IAccount
from gdb.Activity5.account import InvalidAmountException, InsufficientBalanceException, InactiveAccountException


class AbstractAccount(IAccount):
    def __init__(self, account_number, name, age, balance, account_type, status="Active", pin="0000"):
        self._account_number = account_number
        self._name = name
        self._age = age
        self._balance = balance
        self._account_type = account_type
        self._status = status
        self._pin = pin

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot deposit to inactive account: {self._account_number}")
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise InvalidAmountException(f"Deposit amount must be strictly positive: {amount}")
        self._balance += amount

    def withdraw(self, amount):
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")
        if amount > self._balance:
            raise InsufficientBalanceException(f"Insufficient balance. Available: {self._balance}, Requested: {amount}")
        self._balance -= amount