from gdb.Activity11.iaccount import IAccount
from gdb.Activity11.salary_account import SalaryAccount
from gdb.Activity7.saving_account import SavingsAccount
from gdb.Activity7.current_account import CurrentAccount
from gdb.Activity5.account import AccountException


class AccountFactory:

    @staticmethod
    def create_account(account_type: str, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000") -> IAccount:
        t = account_type.strip().upper()

        if t == "SAVINGS":
            return SavingsAccount(account_number, name, age, balance, status, pin, 4.0, 1000.0)
        elif t == "CURRENT":
            return CurrentAccount(account_number, name, age, balance, status, pin, 10000.0)
        elif t == "SALARY":
            return SalaryAccount(account_number, name, age, balance, status, pin)

        raise AccountException(f"Unknown account type: {account_type}")