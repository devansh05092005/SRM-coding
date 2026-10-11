from gdb.Activity4.account import EnhancedAccount

acc = EnhancedAccount(101, "Devansh Singh", 21, 5000.0, "Saving", "4321")

assert acc.validate_pin("4321") is True
assert acc.validate_pin("0000") is False
assert acc.validate_pin(None) is False
print("Test 1: PIN Validation Suite -> PASS")

assert acc.depost(500) is True
assert acc.balance == 5500

assert acc.withdraw(500) is True
assert acc.balance == 5000
print("Test 2: Active Account Transactions -> PASS")


acc._status == "Inactive"

assert acc.deposit(500) is False
assert acc.withdraw(500) is False
assert acc.balance == 5000
print("Test 3: Inactive Protection -> PASS")


print("All Enhanced Account tests passed!")