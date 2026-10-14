from gdb.Activity9.saving_account import SavingsAccount
from gdb.Activity9.current_account import CurrentAccount
from gdb.Activity9.fixed_deposit_account import FixedDepositAccount

def main():
    print("=== Activity 10: Banking Operations Suite ===")

    accounts = [
        SavingsAccount("SA901", 10000.0),
        CurrentAccount("CA902", 50000.0),
        FixedDepositAccount("FD903", 100000.0)
    ]

    for account in accounts:
        account.display_account_info()
        print(f"Interest: Rs {account.calculate_interest()}")

    try:
        account = SavingsAccount("SA904", 1500.0)
        account.withdraw(1000.0)
    except Exception as e:
        if type(e).__name__ == "MinimumBalanceViolationException":
            print(f"PASS: Caught expected MinimumBalanceViolationException -> {e}")
        else:
            raise

    print("All banking operations passed!")

if __name__ == "__main__":
    main()
