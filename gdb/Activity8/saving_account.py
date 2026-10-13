from gdb.Activity1.account import Account
from gdb.Activity5.account import InvalidAmountException, InactiveAccountException, MinimumBalanceViolationException


class SavingsAccount(Account):
    def __init__(self, account_number, name, age, balance, interest_rate=4.0, status="Active", minimum_balance=1000.0):
        super().__init__(account_number, name, age, balance, account_type="Savings", status=status)
        self._interest_rate = interest_rate
        self._minimum_balance = minimum_balance

    def calculate_interest(self):
        return self._balance * self._interest_rate / 100

    def withdraw(self, amount):
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")

        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")

        if self._balance - amount < self._minimum_balance:
            raise MinimumBalanceViolationException(f"Withdrawal would violate minimum balance requirement of Rs {self._minimum_balance}")

        super().withdraw(amount)