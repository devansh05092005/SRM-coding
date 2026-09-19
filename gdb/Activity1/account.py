class Account:
    def __init__(self, account_number, name, age, balance, account_type, status="Active"):
        self._account_number = account_number
        self._name = name
        self._age = age
        self._balance = balance
        self._account_type = account_type
        self._status = status

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def display_account_info(self):
        print(f"The account holder number is: {self._account_number}")
        print(f"The account holder name is: {self._name}")
        print(f"The account holder age is: {self._age}")
        print(f"The account holder number is: {self._balance}")
        print(f"The account holder number is: {self._account_type}")
        print(f"The account holder number is: {self._status}")

    # Account Number Property
    @property
    def account_number(self):
        return self._account_number
    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    # Name Property
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    # Age Property
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value

    # balance Property
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        self._balance = value

    # Account Type Property
    @property
    def account_type(self):
        return self._account_type
    @account_type.setter
    def account_type(self, value):
        self._account_type = value

    # Active Status Property
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value