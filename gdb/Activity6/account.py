from gdb.Activity5.account import EnhancedAccount as Account, InvalidAmountException, InsufficientBalanceException, InactiveAccountException

print("=== Activity 6: Exception Handling Suite ===")

acc = Account(101, "Devansh Singh", 21, 5000.0, "Saving", "4321")

acc.deposit(2000.0)
acc.withdraw(1500.0)

assert acc.balance == 5500.0
print(f"PASS: Valid lifecycle balance: Rs {acc.balance:.1f}")

try:
    acc.deposit(-500.0)
    assert False, "Expected InvalidAmountException"
except InvalidAmountException as e:
    print(f"PASS: Caught InvalidAmountException -> {e}")

acc2 = Account(102, "Jane", 32, 1000.0, "Saving", "1234")

try:
    acc2.withdraw(5000.0)
    assert False, "Expected InsufficientBalanceException"
except InsufficientBalanceException as e:
    print(f"PASS: Caught InsufficientBalanceException -> {e}")

acc3 = Account(104, "Alex", 30, 3000.0, "Saving", "5678",status="Inactive")

try:
    acc3.withdraw(500.0)
    assert False, "Expected InactiveAccountException"
except InactiveAccountException as e:
    print(f"PASS: Caught InactiveAccountException -> {e}")


print("All exception handling tests completed successfully!")