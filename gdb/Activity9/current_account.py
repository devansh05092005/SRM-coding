from gdb.Activity9.band_account import BankAccount

class CurrentAccount(BankAccount):
    def calculate_interest(self) -> float:
        return 0.0

    def get_account_type(self) -> str:
        return "Current"
