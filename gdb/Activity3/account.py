from gdb.Activity1.account import Account as BaseAccount

class EnhancedAccount(BaseAccount):
    def __init__(self, account_number, name, age, balance, account_type, pin, status="Active"):

        if account_number is None or not account_number.strip():
            raise ValueError("Account number cannot be empty")

        if age < 18:
            raise ValueError("Account holder must be at least 18")

        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        if isinstance(pin, str) or len(pin)!=4 or not pin.isdigit():
            raise ValueError("PIN must contain exactly 4 digits")

        super().__init__(account_number, name, age, balance, account_type)

        self._pin = pin


    def validate_pin(self, entered_pin):
        return self._pin == entered_pin

    def deposit(self, amount):
        if self._status.lower()!="active":
            return False

        return super().deposit(amount)

    def withdraw(self, amount):
        if self._status.lower()!="active":
            return False
        
        return super().withdraw(amount)