from gdb.Activity11.abstract_account import AbstractAccount
class SalaryAccount(AbstractAccount):

    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)

    def credit_salary(self, amount):
        return self.deposit(amount)