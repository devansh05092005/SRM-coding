from gdb.Activity1.account import Account

class CurrentAccount(Account):
    def __init__(self, account_number, name, age, balance, overdraft_limit, status="Active"):
        super().__init__(account_number, name, age, balance, account_type="Current", status=status)

        self._overdraft_limit = overdraft_limit