from gdb.Activity9.band_account import BankAccount

class SavingsAccount(BankAccount):
    def calculate_interest(self) -> float:
        return self._balance * 0.04

    def get_account_type(self) -> str:
        return "Savings"
