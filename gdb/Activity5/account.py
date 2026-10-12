from gdb.Activity1.account import Account as BaseAccount

class AccountException(Exception):
    pass
class InvalidAmountException(AccountException):
    pass
class InsufficientBalanceException(AccountException):
    pass
class InactiveAccountException(AccountException):
    pass
class InvalidPinException(AccountException):
    pass
class MinimumBalanceViolationException(AccountException):
    pass


class EnhancedAccount(BaseAccount):
    def __init__(self, account_number, name, age, balance, account_type, pin, status="Active", minimum_balance=0.0):
        if account_number is None or not account_number.strip():
            raise ValueError("Account number cannot be empty")

        if age < 18:
            raise ValueError("Account holder must be at least 18")

        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        if not isinstance(pin, str) or len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must contain exactly 4 digits")

        if minimum_balance < 0 or balance < minimum_balance:
            raise ValueError("Invalid minimum balance")

        super().__init__(account_number, name, age, balance, account_type, status)

        self._pin = pin
        self._minimum_balance = minimum_balance

    def validate_pin(self, entered_pin):
        if not isinstance(entered_pin, str) or entered_pin != self._pin:
            raise InvalidPinException("Invalid PIN")
        return True

    def deposit(self, amount):
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot deposit to inactive account: {self._account_number}")

        if (
            isinstance(amount, bool)
            or not isinstance(amount, (int, float))
            or amount <= 0
        ):
            raise InvalidAmountException(f"Deposit amount must be strictly positive: {amount}")

        self._balance += amount

    def withdraw(self, amount):
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")

        if (
            isinstance(amount, bool)
            or not isinstance(amount, (int, float))
            or amount <= 0
        ):
            raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")

        if amount > self._balance:
            raise InsufficientBalanceException(f"Insufficient balance. Available: {self._balance}, "f"Requested: {amount}")

        if self._balance - amount < self._minimum_balance:
            raise MinimumBalanceViolationException(f"Minimum balance of {self._minimum_balance} must be maintained")

        self._balance -= amount


acc = EnhancedAccount(101, "Devansh Singh", 21, 5000.0, "Saving", "4321")

acc.withdraw(1000.0)

print(f"Successful withdrawal completed: Rs 1000.0 | "f"New Balance: Rs {acc.balance:.1f}")

try:
    acc.deposit(-100.0)
except InvalidAmountException as error:
    print(f"PASS: Caught InvalidAmountException -> {error}")


try:
    acc.withdraw(99999.0)
except InsufficientBalanceException as error:
    print(f"PASS: Caught InsufficientBalanceException -> {error}")
