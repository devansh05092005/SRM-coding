from gdb.Activity11.abstract_account import AbstractAccount


class SalaryAccount(AbstractAccount):
    def __init__(self, account_number, name, age, balance, status="Active", pin="0000"):
        super().__init__(account_number, name, age, balance, "Salary", status, pin)

    def calculate_interest(self):
        return 0.0