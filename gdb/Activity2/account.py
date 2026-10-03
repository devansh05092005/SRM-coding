from gdb.Activity1.account import Account

print("=== Activity 2: Test Account Suite ===")


acc = Account(101, "Devansh Singh", 21, 5000, "Saving")

assert acc.account_number == 101
assert acc.name == "Devansh Singh"
assert acc.age == 21
assert acc.balance == 5000
assert acc.account_type == "Saving"
assert acc.status == "Active"

print(f"Test 1: Initial Account Creation -> PASS [Balance: {acc.balance}]")


res = acc.deposit(1500)
assert res is True
assert acc.balance == 6500

print(f"Test 2: Valid Deposit (+1500.0) -> PASS [New Balance: {acc.balance}]")


res = acc.deposit(-500)
assert res is False
assert acc.balance == 6500

print(f"Test 3: Invalid Deposit (-500.0) -> PASS [Rejected, Balance: {acc.balance}]")


res = acc.withdraw(2000)
assert res is True
assert acc.balance == 4500

print(f"Test 4: Valid Withdrawal (-2000.0) -> PASS [New Balance: {acc.balance}]")


res = acc.withdraw(10000.0)
assert res is False
assert acc.balance == 4500.0

print(f"Test 5: Overdraft Withdrawal (-10000.0) -> PASS [Rejected, Balance: {acc.balance}]")

print("All Account tests completed successfully!")