from gdb.Activity1.account import Account


class SavingsAccount(Account):
    def __init__(self, account_number, name, age, balance, interest_rate, status="Active"):
        super().__init__(account_number, name, age, balance, account_type="Savings", status=status)

        self._interest_rate = interest_rate

    def calculate_interest(self):
        return self._balance * self._interest_rate / 100