from gdb.Activity11.iaccount import IAccount
from gdb.Activity11.savings_account import SavingsAccount
from gdb.Activity11.current_account import CurrentAccount
from gdb.Activity11.salary_account import SalaryAccount


class AccountFactory:

    @staticmethod
    def create_account(account_type,account_number,account_holder,balance=0,**kwargs) -> IAccount:

        account_type = account_type.lower()

        if account_type == "savings":
            return SavingsAccount(account_number,account_holder,balance,**kwargs)

        elif account_type == "current":
            return CurrentAccount(account_number,account_holder,balance,**kwargs)

        elif account_type == "salary":
            return SalaryAccount(account_number,account_holder,balance)

        else:
            raise ValueError(f"Invalid account type: {account_type}")