from abc import abstractmethod
from gdb.Activity11.iaccount import IAccount
class AbstractAccount(IAccount):

    def __init__(self, account_number, account_holder, balance=0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_holder(self):
        return self._account_holder

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount
        return self._balance

    def get_balance(self):
        return self._balance