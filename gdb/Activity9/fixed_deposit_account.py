from gdb.Activity9.band_account import BankAccount

class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        return self._balance * 0.07

    def get_account_type(self):
        return "Fixed Deposit"